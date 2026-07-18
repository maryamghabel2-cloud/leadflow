"""
LeadFlow Autopilot Engine
Runs sales/fulfillment loops with minimal human presence.

What it CAN do unattended (if server is online):
- Capture inbound leads from /hire and demo forms
- Auto-build a personalized clinic demo site for each lead
- Verify USDT payments on-chain
- Auto-fulfill: generate final site + ZIP + delivery page
- Notify admin via Telegram (if TELEGRAM_BOT_TOKEN set)
- Keep operational metrics / order history in SQLite

What it CANNOT do without extra credentials:
- Send WhatsApp / Instagram DMs
- Click Google Search Console buttons (needs Google API OAuth)
- Guarantee traffic while offline SEO is still ramping
"""

from __future__ import annotations

import json
import os
import secrets
import sqlite3
import threading
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from shadow_infiltrator import ShadowInfiltrator


def _now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def _public_base() -> str:
    return os.environ.get("PUBLIC_BASE_URL", "https://leadflow-ai-1vip.onrender.com").rstrip("/")


class AutopilotEngine:
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            db_path = os.environ.get(
                "LEADFLOW_AUTOPILOT_DB",
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "leadflow_autopilot.db"),
            )
        self.db_path = db_path
        self._lock = threading.Lock()
        self.infiltrator = ShadowInfiltrator(output_dir="generated_sites")
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.executescript(
                    """
                    CREATE TABLE IF NOT EXISTS leads (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL,
                        name TEXT,
                        company TEXT,
                        phone TEXT,
                        source TEXT,
                        city TEXT,
                        niche TEXT,
                        notes TEXT,
                        demo_url TEXT,
                        status TEXT DEFAULT 'new',
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_token TEXT UNIQUE NOT NULL,
                        email TEXT,
                        client_name TEXT NOT NULL,
                        plan_name TEXT,
                        amount_usdt REAL NOT NULL,
                        tx_hash TEXT UNIQUE,
                        status TEXT NOT NULL,
                        demo_url TEXT,
                        live_url TEXT,
                        zip_url TEXT,
                        delivery_url TEXT,
                        payload_json TEXT,
                        created_at TEXT NOT NULL,
                        fulfilled_at TEXT
                    );
                    CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        kind TEXT NOT NULL,
                        message TEXT NOT NULL,
                        meta_json TEXT,
                        created_at TEXT NOT NULL
                    );
                    """
                )
                conn.commit()
            finally:
                conn.close()

    def log_event(self, kind: str, message: str, meta: Optional[Dict[str, Any]] = None) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    "INSERT INTO events (kind, message, meta_json, created_at) VALUES (?, ?, ?, ?)",
                    (kind, message, json.dumps(meta or {}, ensure_ascii=False), _now()),
                )
                conn.commit()
            finally:
                conn.close()
        print(f"[AUTOPILOT:{kind}] {message}")

    def notify_admin(self, text: str) -> bool:
        token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
        chat_id = os.environ.get("ADMIN_CHAT_ID", "").strip()
        if not token or not chat_id or token.startswith("DEMO"):
            self.log_event("notify_skip", "Telegram not configured; notification skipped", {"text": text[:200]})
            return False
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            resp = requests.post(
                url,
                json={"chat_id": chat_id, "text": text[:3500], "disable_web_page_preview": True},
                timeout=12,
            )
            ok = resp.status_code == 200
            self.log_event("notify", "Telegram sent" if ok else f"Telegram failed {resp.status_code}", {})
            return ok
        except Exception as e:
            self.log_event("notify_error", str(e))
            return False

    def _slug(self, name: str) -> str:
        return "".join(c if c.isalnum() else "_" for c in (name or "client").lower()).strip("_") or "client"

    def build_demo_for_business(
        self,
        business_name: str,
        city: str = "Dubai",
        niche: str = "Dental Clinic",
        phone: str = "+971 4 555 0100",
    ) -> Dict[str, Any]:
        category = niche or "Dental Clinic"
        low = f"{business_name} {category}".lower()
        if any(k in low for k in ["spa", "aesthetic", "beauty", "skin", "laser"]):
            category = "Spa"
        elif any(k in low for k in ["dental", "dentist", "tooth", "smile", "zahn"]):
            category = "Dental Clinic"
        result = self.infiltrator.generate_luxury_site(
            business_name=business_name or "Clinic Demo",
            category=category,
            city=city or "Dubai",
            phone=phone or "+971 4 555 0100",
        )
        # Prefer same-origin demo path for reliability on Render
        filename = Path(result.get("generated_filename") or "").name.replace("_luxury.html", "_live.html")
        local_live = Path("generated_sites") / "live_demos" / filename
        # ensure live file exists (generator writes via deployer)
        if not local_live.exists():
            # copy luxury to live name if needed
            lux = Path(result.get("generated_filepath") or "")
            if lux.exists():
                local_live.parent.mkdir(parents=True, exist_ok=True)
                local_live.write_text(lux.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        demo_path = f"/live_demos/{local_live.name}" if local_live.exists() else result.get("live_cloud_demo_url")
        demo_url = demo_path if str(demo_path).startswith("http") else f"{_public_base()}{demo_path}"
        zip_name = Path(result.get("client_handover_zip") or "").name
        zip_url = f"{_public_base()}/handover_packages/{zip_name}" if zip_name else None
        out = {
            "status": "success",
            "business_name": business_name,
            "demo_url": demo_url,
            "demo_path": demo_path,
            "zip_url": zip_url,
            "zip_path": result.get("client_handover_zip"),
            "paradigm": result.get("industry_paradigm_applied"),
        }
        self.log_event("demo_built", f"Demo built for {business_name}", out)
        return out

    def ingest_lead(
        self,
        email: str,
        name: str = "",
        company: str = "",
        phone: str = "",
        source: str = "unknown",
        city: str = "Dubai",
        niche: str = "Dental Clinic",
        notes: str = "",
        auto_demo: bool = True,
    ) -> Dict[str, Any]:
        email = (email or "").strip().lower()
        company = (company or name or "New Clinic").strip()
        demo_url = None
        demo_meta: Dict[str, Any] = {}
        status = "new"

        if auto_demo and company:
            try:
                demo_meta = self.build_demo_for_business(
                    business_name=company,
                    city=city or "Dubai",
                    niche=niche or "Dental Clinic",
                    phone=phone or "+971 4 555 0100",
                )
                demo_url = demo_meta.get("demo_url")
                status = "demo_ready"
            except Exception as e:
                self.log_event("demo_error", f"Demo failed for {company}: {e}")
                status = "demo_failed"

        with self._lock:
            conn = self._connect()
            try:
                cur = conn.execute(
                    """
                    INSERT INTO leads (email, name, company, phone, source, city, niche, notes, demo_url, status, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        email,
                        name.strip(),
                        company,
                        phone.strip(),
                        source,
                        city,
                        niche,
                        notes,
                        demo_url,
                        status,
                        _now(),
                        _now(),
                    ),
                )
                conn.commit()
                lead_id = cur.lastrowid
            finally:
                conn.close()

        msg = (
            f"🚀 NEW LEAD #{lead_id}\n"
            f"Name: {name}\nCompany: {company}\nEmail: {email}\nPhone: {phone}\n"
            f"City/Niche: {city} / {niche}\nSource: {source}\n"
            f"Demo: {demo_url or 'n/a'}\n"
            f"Checkout: {_public_base()}/onboard\n"
            f"Hire: {_public_base()}/hire"
        )
        self.notify_admin(msg)
        self.log_event("lead", f"Lead #{lead_id} {company}", {"lead_id": lead_id, "demo_url": demo_url})

        return {
            "status": "success",
            "lead_id": lead_id,
            "company": company,
            "demo_url": demo_url,
            "checkout_url": f"{_public_base()}/onboard",
            "hire_url": f"{_public_base()}/hire",
            "autopilot": "lead_ingested_demo_ready" if demo_url else status,
            "demo_meta": demo_meta,
        }

    def fulfill_payment(
        self,
        *,
        client_name: str,
        amount_usdt: float,
        tx_hash: str,
        email: str = "",
        plan_name: str = "",
        city: str = "Dubai",
        niche: str = "Dental Clinic",
        phone: str = "+971 4 555 0100",
    ) -> Dict[str, Any]:
        client_name = (client_name or "Client Clinic").strip()
        plan_name = plan_name or f"{amount_usdt} USDT package"
        token = secrets.token_urlsafe(16)

        # Build / refresh deliverable
        demo_meta = self.build_demo_for_business(client_name, city=city, niche=niche, phone=phone)
        live_url = demo_meta.get("demo_url")
        zip_url = demo_meta.get("zip_url")
        delivery_url = f"{_public_base()}/delivery/{token}"

        payload = {
            "client_name": client_name,
            "amount_usdt": amount_usdt,
            "tx_hash": tx_hash,
            "plan_name": plan_name,
            "live_url": live_url,
            "zip_url": zip_url,
            "delivery_url": delivery_url,
            "support_note": "Autopilot fulfillment completed. Customize content/branding as needed.",
        }

        with self._lock:
            conn = self._connect()
            try:
                # idempotent on tx_hash
                existing = conn.execute("SELECT * FROM orders WHERE tx_hash = ?", (tx_hash,)).fetchone()
                if existing:
                    return dict(existing)
                conn.execute(
                    """
                    INSERT INTO orders
                    (order_token, email, client_name, plan_name, amount_usdt, tx_hash, status,
                     demo_url, live_url, zip_url, delivery_url, payload_json, created_at, fulfilled_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        token,
                        (email or "").strip().lower(),
                        client_name,
                        plan_name,
                        float(amount_usdt or 0),
                        tx_hash,
                        "fulfilled",
                        live_url,
                        live_url,
                        zip_url,
                        delivery_url,
                        json.dumps(payload, ensure_ascii=False),
                        _now(),
                        _now(),
                    ),
                )
                conn.commit()
            finally:
                conn.close()

        # Write a static delivery receipt snapshot too
        receipt_dir = Path("generated_sites") / "orders"
        receipt_dir.mkdir(parents=True, exist_ok=True)
        (receipt_dir / f"{token}.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

        notify = (
            f"✅ PAYMENT FULFILLED\n"
            f"Client: {client_name}\n"
            f"Amount: {amount_usdt} USDT\n"
            f"Plan: {plan_name}\n"
            f"TX: {tx_hash}\n"
            f"Live: {live_url}\n"
            f"ZIP: {zip_url}\n"
            f"Delivery: {delivery_url}"
        )
        self.notify_admin(notify)
        self.log_event("fulfill", f"Order fulfilled for {client_name}", payload)

        return {
            "status": "fulfilled",
            "order_token": token,
            "delivery_url": delivery_url,
            "live_url": live_url,
            "zip_url": zip_url,
            "client_name": client_name,
            "amount_usdt": amount_usdt,
            "tx_hash": tx_hash,
            "plan_name": plan_name,
        }

    def get_order_by_token(self, token: str) -> Optional[Dict[str, Any]]:
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute("SELECT * FROM orders WHERE order_token = ?", (token,)).fetchone()
                return dict(row) if row else None
            finally:
                conn.close()

    def list_leads(self, limit: int = 50) -> List[Dict[str, Any]]:
        with self._lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    "SELECT * FROM leads ORDER BY id DESC LIMIT ?",
                    (limit,),
                ).fetchall()
                return [dict(r) for r in rows]
            finally:
                conn.close()

    def list_orders(self, limit: int = 50) -> List[Dict[str, Any]]:
        with self._lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    "SELECT * FROM orders ORDER BY id DESC LIMIT ?",
                    (limit,),
                ).fetchall()
                return [dict(r) for r in rows]
            finally:
                conn.close()

    def list_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self._lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    "SELECT * FROM events ORDER BY id DESC LIMIT ?",
                    (limit,),
                ).fetchall()
                return [dict(r) for r in rows]
            finally:
                conn.close()

    def status_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            conn = self._connect()
            try:
                leads = conn.execute("SELECT COUNT(*) AS c FROM leads").fetchone()["c"]
                orders = conn.execute("SELECT COUNT(*) AS c FROM orders").fetchone()["c"]
                fulfilled = conn.execute(
                    "SELECT COUNT(*) AS c FROM orders WHERE status = 'fulfilled'"
                ).fetchone()["c"]
                revenue = conn.execute(
                    "SELECT COALESCE(SUM(amount_usdt),0) AS s FROM orders WHERE status = 'fulfilled'"
                ).fetchone()["s"]
            finally:
                conn.close()
        telegram_ready = bool(
            os.environ.get("TELEGRAM_BOT_TOKEN")
            and os.environ.get("ADMIN_CHAT_ID")
            and not os.environ.get("TELEGRAM_BOT_TOKEN", "").startswith("DEMO")
        )
        treasury = os.environ.get("TRON_TREASURY_WALLET_ADDRESS", "").strip()
        return {
            "autopilot": "online",
            "mode": "inbound_self_serve",
            "public_base": _public_base(),
            "leads_total": leads,
            "orders_total": orders,
            "orders_fulfilled": fulfilled,
            "revenue_usdt": revenue,
            "telegram_ready": telegram_ready,
            "payments_ready": bool(treasury),
            "capabilities": {
                "inbound_lead_capture": True,
                "auto_demo_generation": True,
                "usdt_payment_verification": True,
                "auto_fulfillment_zip_delivery": True,
                "telegram_admin_alerts": telegram_ready,
                "whatsapp_instagram_outbound": False,
                "google_search_console_clicks": False,
            },
            "needs_for_full_outbound_automation": [
                "WhatsApp Business API credentials OR Email API (Resend/SendGrid)",
                "Optional: Google Indexing API service account for Search Console automation",
            ],
            "unattended_sales_path": [
                "Visitor lands on /hire or /blog from SEO/social",
                "Submits form -> autopilot builds demo + stores lead + Telegram alert",
                "Visitor pays USDT on /onboard -> chain verify -> auto delivery page/ZIP",
                "You collect money without being online (if Telegram configured, you get pinged)",
            ],
        }

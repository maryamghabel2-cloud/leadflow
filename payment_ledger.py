"""
LeadFlow.AI - Payment ledger for replay protection and audit trail.
Persists verified transaction hashes so the same on-chain payment cannot unlock product twice.
"""

from __future__ import annotations

import os
import sqlite3
import threading
from datetime import datetime
from typing import Any, Dict, Optional


class PaymentLedger:
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            db_path = os.environ.get(
                "LEADFLOW_PAYMENT_DB",
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "leadflow_payments.db"),
            )
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS processed_payments (
                        tx_hash TEXT PRIMARY KEY,
                        amount_usdt REAL NOT NULL,
                        sender TEXT,
                        receiver TEXT,
                        client_name TEXT,
                        plan_name TEXT,
                        status TEXT NOT NULL,
                        created_at TEXT NOT NULL
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS captured_leads (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL,
                        name TEXT,
                        company TEXT,
                        source_studio TEXT,
                        created_at TEXT NOT NULL
                    )
                    """
                )
                conn.commit()
            finally:
                conn.close()

    def has_processed(self, tx_hash: str) -> bool:
        tx_hash = (tx_hash or "").strip()
        if not tx_hash:
            return False
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    "SELECT 1 FROM processed_payments WHERE tx_hash = ? LIMIT 1",
                    (tx_hash,),
                ).fetchone()
                return row is not None
            finally:
                conn.close()

    def record_success(
        self,
        tx_hash: str,
        amount_usdt: float,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        client_name: Optional[str] = None,
        plan_name: Optional[str] = None,
        status: str = "success",
    ) -> Dict[str, Any]:
        tx_hash = (tx_hash or "").strip()
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO processed_payments
                    (tx_hash, amount_usdt, sender, receiver, client_name, plan_name, status, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        tx_hash,
                        float(amount_usdt or 0),
                        sender,
                        receiver,
                        client_name,
                        plan_name,
                        status,
                        now,
                    ),
                )
                conn.commit()
                return {"recorded": True, "tx_hash": tx_hash, "created_at": now}
            except sqlite3.IntegrityError:
                return {"recorded": False, "tx_hash": tx_hash, "reason": "duplicate"}
            finally:
                conn.close()

    def capture_lead(
        self,
        email: str,
        name: str = "",
        company: str = "",
        source_studio: str = "UNKNOWN",
    ) -> Dict[str, Any]:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        with self._lock:
            conn = self._connect()
            try:
                cur = conn.execute(
                    """
                    INSERT INTO captured_leads (email, name, company, source_studio, created_at)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (email.strip().lower(), name.strip(), company.strip(), source_studio, now),
                )
                conn.commit()
                return {
                    "status": "success",
                    "lead_id": f"lead_{cur.lastrowid}",
                    "email": email.strip().lower(),
                    "created_at": now,
                }
            finally:
                conn.close()

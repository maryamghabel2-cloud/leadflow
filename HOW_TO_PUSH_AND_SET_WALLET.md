# چطور تغییرات را به GitHub بفرستی + کجا ولت را بگذاری

## بخش A — من چرا خودم push نمی‌کنم؟

این محیط به اکانت GitHub تو لاگین نیست. برای push نیاز است یکی از این‌ها:

1. **خودت از لپ‌تاپ/Codespace** push کنی (امن‌ترین و توصیه‌شده)، یا  
2. یک **Personal Access Token (PAT)** با دسترسی `repo` بسازی و **فقط در محیط امن خودت** استفاده کنی.

⚠️ **هرگز توکن یا کلید خصوصی ولت را در چت عمومی نفرست.**  
اگر توکن را اینجا بفرستی ممکن است لو برود. برای push، توکن را فقط داخل ترمینال خودت بگذار.

---

## بخش B — روش توصیه‌شده: push از سیستم خودت

### B1) کد fixed را بگیر

اگر فقط روی GitHub کار می‌کنی و فایل‌های workspace Arena را نداری:

**گزینه ۱ (اگر همین پروژه را در Arena داری):**  
فایل‌های تغییرکرده را از workspace دانلود/کپی کن روی کلون لوکال.

**گزینه ۲ (سریع):**  
در سیستم خودت:

```bash
git clone https://github.com/maryamghabel2-cloud/leadflow.git
cd leadflow
```

سپس فایل‌های جدید/تغییریافته را از این لیست جایگزین کن (از خروجی Arena یا zip):

**Modified**
- `blockchain_verifier.py`
- `web_app.py`
- `onboard.html`
- `no_website_miner.py`
- `cloud_deployer.py`
- `docker-compose.yml`
- `render.yaml`
- `requirements.txt`
- `.gitignore`
- `docs/first_100_outbound_campaign_ledger.json`

**New**
- `payment_ledger.py`
- `README.md`
- `CEO_AUDIT_REPORT.md`
- `LAUNCH_AND_REVENUE_PLAYBOOK.md`
- `HOW_TO_PUSH_AND_SET_WALLET.md` (همین فایل)
- `.env.example`
- `agents/` (کل پوشه)
- `tests/` (کل پوشه)

### B2) commit و push

```bash
cd leadflow

git checkout -b fix/payment-hardening-launch
# یا مستقیم روی main اگر ترجیح می‌دهی:
# git checkout main

git add \
  blockchain_verifier.py web_app.py onboard.html no_website_miner.py \
  cloud_deployer.py docker-compose.yml render.yaml requirements.txt \
  .gitignore docs/first_100_outbound_campaign_ledger.json \
  payment_ledger.py README.md CEO_AUDIT_REPORT.md \
  LAUNCH_AND_REVENUE_PLAYBOOK.md HOW_TO_PUSH_AND_SET_WALLET.md \
  .env.example agents tests

git status

git commit -m "$(cat <<'EOF'
fix: harden USDT payments, honest offer, agent fleet, tests

- Block SIM_TRON_ bypass in production
- Enforce treasury wallet match + replay protection
- Stop hardcoding USDT contract as deposit address
- Add public config endpoint, README, CEO audit, launch playbook
EOF
)"

git push -u origin HEAD
```

اگر GitHub ازت لاگین خواست:
- **HTTPS + PAT:** Settings → Developer settings → Personal access tokens → Fine-grained یا classic با scope `repo`
- یا **SSH key** به اکانت اضافه کن

### B3) روی GitHub چک کن
باز کن: `https://github.com/maryamghabel2-cloud/leadflow`  
باید commit جدید / PR را ببینی. اگر branch زدی، Merge Pull Request بزن روی `main`.

---

## بخش C — کجا آدرس ولت را بگذاری؟ (خیلی مهم)

### ❌ جاهایی که **نباید** ولت را بگذاری
- داخل `onboard.html` به‌صورت hardcode دائمی (دیگر لازم نیست؛ از API می‌خواند)
- داخل کد Python commit‌شده
- داخل README عمومی اگر نمی‌خواهی عمومی باشد (اختیاری است)
- داخل چت / اسکرین‌شات عمومی همراه با seed/private key

### ✅ جای درست: Environment Variable روی سرور

نام متغیر:

```text
TRON_TREASURY_WALLET_ADDRESS
```

مقدار:

```text
Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

(آدرس Tron تو که با `T` شروع می‌شود — **آدرس عمومی ولت**، نه seed و نه private key)

---

## بخش D — تنظیم روی Render (پیشنهادی)

1. برو به [https://dashboard.render.com](https://dashboard.render.com)
2. **New → Web Service**
3. Connect GitHub repo: `maryamghabel2-cloud/leadflow`
4. Branch: `main`
5. Runtime: **Docker** (Dockerfile موجود است) یا طبق `render.yaml`
6. بعد از ساخت سرویس → تب **Environment** این‌ها را Add کن:

| Key | Value | Secret؟ |
|---|---|---|
| `LEADFLOW_ENV` | `production` | No |
| `LEADFLOW_ALLOW_SIM_PAYMENTS` | `false` | No |
| `LEADFLOW_ALLOW_FAKE_LEADS` | `false` | No |
| `CLOUD_AUTO_PUSH` | `false` | No |
| `TRON_TREASURY_WALLET_ADDRESS` | `T...آدرس_ولت_تو...` | Yes (ترجیحاً) |
| `TELEGRAM_BOT_TOKEN` | توکن ربات (اختیاری) | Yes |
| `ADMIN_CHAT_ID` | chat id عددی (اختیاری) | Yes |
| `PORT` | `8000` | No |

7. **Save / Deploy**
8. بعد از سبز شدن سرویس، این URLها را تست کن:

```text
https://YOUR-SERVICE.onrender.com/api/health
https://YOUR-SERVICE.onrender.com/api/config/public
https://YOUR-SERVICE.onrender.com/onboard
```

### انتظار درست
- `/api/health` → `"treasury_configured": true`
- `/api/config/public` → فیلد `treasury_wallet` همان آدرس `T...` تو
- صفحه `/onboard` → همان آدرس را نشان دهد (نه `TR7NHqje...`)
- `POST /api/verify-payment` با `SIM_TRON_test` → **fail** در production

---

## بخش E — تنظیم لوکال (فقط برای تست روی لپ‌تاپ)

```bash
cd leadflow
cp .env.example .env
# فایل .env را باز کن و پر کن:
# TRON_TREASURY_WALLET_ADDRESS=TYourWallet
# LEADFLOW_ENV=development
# LEADFLOW_ALLOW_SIM_PAYMENTS=true   # فقط لوکال

python3 -m venv .venv
source .venv/bin/activate   # ویندوز: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn web_app:app --host 0.0.0.0 --port 8000
```

باز کن: http://localhost:8000/onboard

> `.env` داخل `.gitignore` است و push نمی‌شود. همین درست است.

---

## بخش F — تست پول واقعی (۱ USDT)

1. از TronLink (یا هر ولت) **۱ USDT روی شبکه TRC-20** به همان `TRON_TREASURY_WALLET_ADDRESS` بفرست.
2. TXID را از Tronscan کپی کن.
3. در `/onboard` پیست کن و Verify بزن.
4. باید success واقعی بیاید.
5. **همان TXID را دوباره** بفرست → باید `replay_rejected` شود.

اگر Telegram را ست کرده باشی، پیام واریز می‌آید.

---

## بخش G — چک‌لیست «الان پول می‌توانم بگیرم؟»

- [ ] کد hardened روی `main` گیت‌هاب است  
- [ ] Render (یا Docker VPS) با envهای production بالا است  
- [ ] `TRON_TREASURY_WALLET_ADDRESS` = ولت واقعی تو  
- [ ] `/api/config/public` ولت درست را نشان می‌دهد  
- [ ] SIM payment در production رد می‌شود  
- [ ] تست ۱ USDT واقعی پاس شده  
- [ ] لندینگ/outreach فقط offerی $499 را می‌فروشد  

وقتی همه تیک خورد → برو سراغ `agents/04_revenue_ops_agent.md` برای فروش.

---

## بخش H — اگر می‌خواهی من push را «تقریباً خودکار» کنم

من می‌توانم در workspace همین‌جا `git commit` محلی بسازم.  
برای `git push` به ریپوی تو یکی از این‌ها لازم است:

1. تو خودت push کنی (بهترین)، یا  
2. در **سیستم خودت** این را اجرا کنی (توکن را فقط لوکال بگذار):

```bash
git push https://<YOUR_GITHUB_USERNAME>:<YOUR_PAT>@github.com/maryamghabel2-cloud/leadflow.git main
```

یا SSH:

```bash
git remote set-url origin git@github.com:maryamghabel2-cloud/leadflow.git
git push origin main
```

**Private key ولت / seed phrase را هرگز برای من یا هیچ‌کس نفرست.**  
فقط **آدرس عمومی** (`T...`) برای env کافی است.

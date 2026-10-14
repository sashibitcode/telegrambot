# 🤖 ShashikantPortfolioBot - Telegram Portfolio Assistant

An interactive, asynchronous Telegram Bot built with Python and `python-telegram-bot` to showcase **Shashikant Raj's** verified Data Analyst portfolio, skills inventory, featured projects, and certifications.

---

## ✨ Features

- 👤 **About Me**: Academic credentials from Jagannath University, Jaipur, and professional background.
- 🛠 **Skills Inventory**: Categorized breakdown of Python, SQL, Power BI, Excel, Pandas, and Machine Learning.
- 🚀 **Projects Showcase**: Interactive cards for **SAS.AI**, **QuickDownload**, **Blinkit Grocery Analytics**, **Global COVID-19 Timeseries SQL Analysis**, and **IPL Telemetry**, complete with direct **Live Demo** and **GitHub** buttons.
- 🏆 **Certifications**: One-click verification for Cisco PCAP Python, HackerRank SQL (Intermediate), and Forage credentials.
- 📄 **Resume Access**: Quick link to view and download the verified resume.
- 📬 **Recruiter Message Forwarder**: Visitors and recruiters can type any inquiry directly in Telegram, and it will be forwarded straight to your personal Telegram account!

---

## 🚀 Quick Setup Guide

### 1. Create your Bot with `@BotFather`
1. Open your Telegram app and search for **`@BotFather`** (verified checkmark).
2. Send `/newbot`.
3. Enter a display name, for example: `Shashikant Raj Portfolio`.
4. Enter a username ending in `bot`, for example:
   - `ShashikantPortfolioBot`
   - `ShashiPortfolioBot`
   - `sashibitcode_bot`
5. `@BotFather` will reply with your **HTTP API Token**:
   ```
   Use this token to access the HTTP API:
   7123456789:AAH...
   ```

### 2. Configure Environment Variables
Open the `.env` file in this directory and paste your token:
```env
TELEGRAM_BOT_TOKEN=7123456789:AAH...

# Optional: Add your personal Telegram chat ID to receive visitor messages
# Message @userinfobot on Telegram to get your numeric ID
ADMIN_CHAT_ID=123456789
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run Dry-Run Tests
Verify that all data structures and keyboards are intact:
```powershell
python bot.py --test
```

### 5. Start the Bot
```powershell
python bot.py
```
Open Telegram, search for your bot username, and tap **Start** (or send `/start`)!

---

## ⌨️ Command & Navigation Reference

| Menu Button | Command | Action |
| :--- | :--- | :--- |
| `👤 About Me` | `/about` | Bio, education at Jagannath University, and internship experience. |
| `🛠 Skills` | `/skills` | Complete categorized technical skills matrix. |
| `🚀 Projects` | `/projects` | Showcase of 5 projects with Live Demo & GitHub code buttons. |
| `🏆 Certifications`| `/certifications`| Verified credentials with direct verification links. |
| `📄 Resume` | `/resume` | Link to view and download the verified 2026 CV. |
| `📬 Contact / Hire`| `/contact` | Social profiles + direct messaging flow. |
| — | `/help` | Complete help guide. |

---

## 🌐 24/7 Cloud Deployment Options

To keep the bot running 24/7 without keeping your computer on:
1. **Render / Railway / fly.io**:
   - Create a background worker service.
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python bot.py`
   - Add `TELEGRAM_BOT_TOKEN` in the environment variables tab.
2. **VPS (Ubuntu / Debian)**:
   - Run with `systemd` or `pm2`:
     ```bash
     pm2 start bot.py --name "portfolio-bot" --interpreter python3
     ```

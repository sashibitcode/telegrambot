"""
Start and Help command handlers.
"""

import os
from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA
from keyboards.menus import get_main_keyboard


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command and alerts admin of new visitors."""
    personal = PORTFOLIO_DATA["personal"]
    sender = update.effective_user
    admin_chat_id = os.getenv("ADMIN_CHAT_ID")

    sender_name = sender.full_name or "Anonymous"
    sender_username = f"@{sender.username}" if sender.username else "No username"

    # Send visitor alert to admin (if sender is not admin himself)
    if admin_chat_id and str(sender.id) != str(admin_chat_id):
        try:
            alert_text = (
                f"👁️ *New Visitor Alert!*\n\n"
                f"Someone just opened your Portfolio Bot!\n"
                f"👤 *Name:* {sender_name}\n"
                f"🏷️ *Username:* {sender_username}\n"
                f"🆔 *User ID:* `{sender.id}`"
            )
            await context.bot.send_message(
                chat_id=admin_chat_id,
                text=alert_text,
                parse_mode="Markdown"
            )
        except Exception:
            pass

    welcome_text = (
        f"👋 *Welcome to {personal['name']}'s Portfolio Bot!*\n\n"
        f"💼 *Role:* {personal['title']}\n"
        f"📍 *Location:* {personal['location']}\n"
        f"🎯 *Headline:* _{personal['headline']}_\n"
        f"🟢 *Status:* {personal['status']}\n\n"
        "Explore my portfolio interactively using the quick-action menu buttons below:\n\n"
        "• 👤 *About Me* — Background, university education, and experience\n"
        "• 🛠 *Skills* — Categorized programming languages, SQL & analytics tools\n"
        "• 🚀 *Projects* — Live demos, GitHub repos, and architecture summaries\n"
        "• 🏆 *Certifications* — Cisco PCAP, HackerRank SQL, and Forage credentials\n"
        "• 📄 *Resume* — Direct download and verified resume link\n"
        "• 📬 *Contact / Hire* — Send a direct inquiry to me on Telegram"
    )

    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )


async def myid_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Replies with the sender's Telegram chat ID to easily configure ADMIN_CHAT_ID."""
    user = update.effective_user
    text = (
        f"🆔 *Your Telegram Chat ID:* `{user.id}`\n\n"
        f"Copy this number and set it as `ADMIN_CHAT_ID={user.id}` in your `.env` file.\n"
        f"Once set, whenever anyone visits your bot or sends a message, you will get an instant alert here!"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /help command."""
    help_text = (
        "💡 *How to use ShashikantPortfolioBot:*\n\n"
        "You can either tap the menu buttons on your keyboard or use these commands:\n"
        "• `/start` — Main welcome message and keyboard\n"
        "• `/about` — Read candidate bio and academic background\n"
        "• `/skills` — View technical skill matrix\n"
        "• `/projects` — Explore featured projects with live links\n"
        "• `/certifications` — View certified credentials\n"
        "• `/resume` — Access the latest resume\n"
        "• `/contact` — Connect via LinkedIn, GitHub, or send a message"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown", reply_markup=get_main_keyboard())

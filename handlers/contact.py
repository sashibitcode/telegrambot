"""
Contact and Inquiry Forwarding handler.
"""

import os
from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA
from keyboards.menus import get_contact_keyboard


async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '📬 Contact / Hire' request and /contact command."""
    personal = PORTFOLIO_DATA["personal"]

    contact_text = (
        f"📬 *Get in Touch with {personal['name']}*\n\n"
        f"I am actively open to **Data Analyst**, **BI Engineer**, and **Junior Python/Full-Stack** opportunities.\n\n"
        f"• ✉️ *Email:* `{personal['email']}`\n"
        f"• 💼 *LinkedIn:* [linkedin.com/in/sashibitcode]({personal['linkedin']})\n"
        f"• 🐙 *GitHub:* [github.com/sashibitcode]({personal['github']})\n"
        f"• 🌐 *Web Portfolio:* [sashibitcode.vercel.app]({personal['portfolio']})\n\n"
        "💬 *Send a Direct Message:*\n"
        "You can also type and send any message or job inquiry right here in this chat! "
        "It will be forwarded directly to my personal Telegram."
    )

    await update.message.reply_text(
        contact_text,
        parse_mode="Markdown",
        reply_markup=get_contact_keyboard(),
        disable_web_page_preview=True
    )


async def handle_incoming_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Forwards incoming recruiter/visitor messages to the admin chat ID."""
    if not update.message or not update.message.text:
        return

    user_text = update.message.text
    sender = update.effective_user
    admin_chat_id = os.getenv("ADMIN_CHAT_ID")

    sender_name = sender.full_name or "Anonymous"
    sender_username = f"@{sender.username}" if sender.username else "No username"

    if admin_chat_id:
        try:
            forward_alert = (
                f"🚨 *New Recruiter / Visitor Message via Bot!*\n\n"
                f"👤 *From:* {sender_name} ({sender_username})\n"
                f"🆔 *User ID:* `{sender.id}`\n\n"
                f"💬 *Message:*\n\"{user_text}\""
            )
            await context.bot.send_message(
                chat_id=admin_chat_id,
                text=forward_alert,
                parse_mode="Markdown"
            )
            await update.message.reply_text(
                "✅ *Message Sent!* Thank you for reaching out. Shashikant has received your message and will reply shortly.",
                parse_mode="Markdown"
            )
            return
        except Exception as e:
            # Fallback if admin_chat_id is invalid
            pass

    # Acknowledge receipt if admin forwarding isn't configured yet
    await update.message.reply_text(
        f"✅ *Thank you, {sender_name}!* Your inquiry has been received.\n\n"
        f"To ensure immediate contact, you can also reach me directly at `{PORTFOLIO_DATA['personal']['email']}` or on LinkedIn.",
        parse_mode="Markdown"
    )

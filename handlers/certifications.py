"""
Certifications handler.
"""

from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA
from keyboards.menus import get_certifications_keyboard


async def certifications_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '🏆 Certifications' request and /certifications command."""
    certs = PORTFOLIO_DATA["certifications"]

    message_lines = [
        "🏆 *Verified Certifications & Credentials*\n",
        "Tap the buttons below to verify each credential directly on Cisco, HackerRank, and Forage:\n"
    ]

    for idx, c in enumerate(certs, 1):
        message_lines.append(f"*{idx}. {c['title']}*")
        message_lines.append(f"   🏛 *Issuer:* {c['issuer']}")
        message_lines.append(f"   📅 *Issued:* {c['date']}\n")

    keyboard = get_certifications_keyboard(certs)

    await update.message.reply_text(
        "\n".join(message_lines),
        parse_mode="Markdown",
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

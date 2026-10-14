"""
Projects showcase handler.
"""

from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA
from keyboards.menus import get_project_keyboard


async def projects_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '🚀 Projects' request and /projects command."""
    projects = PORTFOLIO_DATA["projects"]

    await update.message.reply_text(
        "🚀 *Featured Projects & Case Studies*\n\n"
        "Here are my top production applications and data analytics solutions. Tap the buttons below each card to view live demos or explore source code:",
        parse_mode="Markdown"
    )

    for p in projects:
        tech_list = " · ".join(p["tech"])
        card_text = (
            f"📦 *{p['title']}*\n"
            f"_{p['tagline']}_\n\n"
            f"{p['summary']}\n\n"
            f"🛠 *Tech Stack:* `{tech_list}`"
        )

        keyboard = get_project_keyboard(p)
        await update.message.reply_text(
            card_text,
            parse_mode="Markdown",
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

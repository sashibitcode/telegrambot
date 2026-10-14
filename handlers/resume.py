"""
Resume handler.
"""

from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA
from keyboards.menus import get_resume_keyboard


async def resume_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '📄 Resume' request and /resume command."""
    personal = PORTFOLIO_DATA["personal"]

    resume_text = (
        f"📄 *{personal['name']} — Curriculum Vitae*\n\n"
        f"🎯 *Target Domain:* Data Analyst / Business Intelligence / Python Developer\n"
        f"🎓 *Education:* B.Tech CSE (2022 - 2026), Jagannath University, Jaipur\n"
        f"⭐ *Key Highlights:*\n"
        f"  • Production experience with Next.js, Python FastAPI, and yt-dlp pipelines\n"
        f"  • Power BI & SQL dashboard design analyzing over $1.29M in transaction records\n"
        f"  • Cisco Certified PCAP & HackerRank SQL (Intermediate)\n\n"
        f"Click the button below to view and download the verified resume from the web portfolio:"
    )

    await update.message.reply_text(
        resume_text,
        parse_mode="Markdown",
        reply_markup=get_resume_keyboard(),
        disable_web_page_preview=True
    )

"""
About Me handler.
"""

from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA


async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '👤 About Me' request and /about command."""
    personal = PORTFOLIO_DATA["personal"]
    about = PORTFOLIO_DATA["about"]
    edu = about["education"]
    exp = about["experience"]

    coursework_str = ", ".join(edu["coursework"])
    exp_bullets = "\n".join([f"  • {pt}" for pt in exp["points"]])

    text = (
        f"👤 *About {personal['name']}*\n"
        f"_{personal['title']} · {personal['handle']}_\n\n"
        f"{about['summary']}\n\n"
        f"🎓 *Academic Background:*\n"
        f"• *Degree:* {edu['degree']}\n"
        f"• *Institution:* {edu['institution']}\n"
        f"• *Duration:* {edu['duration']}\n"
        f"• *Core Subjects:* {coursework_str}\n\n"
        f"💼 *Professional Experience:*\n"
        f"• *Role:* {exp['role']}\n"
        f"• *Company:* {exp['company']} ({exp['duration']})\n"
        f"{exp_bullets}\n\n"
        f"📍 *Location:* {personal['location']}\n"
        f"🌐 *Web Portfolio:* [sashibitcode.vercel.app]({personal['portfolio']})"
    )

    await update.message.reply_text(text, parse_mode="Markdown", disable_web_page_preview=True)

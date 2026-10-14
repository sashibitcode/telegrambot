"""
Technical skills handler.
"""

from telegram import Update
from telegram.ext import ContextTypes
from data.portfolio_data import PORTFOLIO_DATA


async def skills_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the '🛠 Skills' request and /skills command."""
    skills_data = PORTFOLIO_DATA["skills"]

    message_lines = [
        "🛠 *Technical Skills Inventory*\n",
        "A categorized overview of programming languages, analytical frameworks, and visualization tools:\n"
    ]

    icons = {
        "Programming & Querying": "💻",
        "Data Analysis & Modeling": "📊",
        "Visualization & BI Tools": "📈",
        "Engineering & Cloud": "⚙️"
    }

    for category, skills in skills_data.items():
        icon = icons.get(category, "🔹")
        message_lines.append(f"{icon} *{category}*")
        for skill in skills:
            message_lines.append(f"  • {skill}")
        message_lines.append("")

    message_lines.append("🎯 *Focus Areas:* Data Cleaning, Relational SQL Modeling, Power BI Dashboards & Generative AI Pipelines.")

    await update.message.reply_text("\n".join(message_lines), parse_mode="Markdown")

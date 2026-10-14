"""
Interactive keyboards for ShashikantPortfolioBot.
Provides ReplyKeyboards for navigation and InlineKeyboards for action links.
"""

from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from data.portfolio_data import PORTFOLIO_DATA


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Returns the persistent bottom navigation keyboard."""
    keyboard = [
        [KeyboardButton("👤 About Me"), KeyboardButton("🛠 Skills")],
        [KeyboardButton("🚀 Projects"), KeyboardButton("🏆 Certifications")],
        [KeyboardButton("📄 Resume"), KeyboardButton("📬 Contact / Hire")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)


def get_project_keyboard(project: dict) -> InlineKeyboardMarkup:
    """Builds inline action buttons for a single project."""
    buttons = []
    if project.get("live"):
        buttons.append(InlineKeyboardButton("🌐 Live Demo", url=project["live"]))
    if project.get("github"):
        buttons.append(InlineKeyboardButton("💻 GitHub Code", url=project["github"]))

    # 2 buttons per row
    return InlineKeyboardMarkup([buttons])


def get_certifications_keyboard(certifications: list) -> InlineKeyboardMarkup:
    """Builds verification link buttons for certifications."""
    buttons = []
    for cert in certifications:
        if cert.get("credential"):
            # Truncated title for button
            btn_title = cert["title"]
            if len(btn_title) > 28:
                btn_title = btn_title[:25] + "..."
            buttons.append([InlineKeyboardButton(f"📜 {btn_title}", url=cert["credential"])])
    return InlineKeyboardMarkup(buttons)


def get_contact_keyboard() -> InlineKeyboardMarkup:
    """Builds direct link buttons for social and portfolio profiles."""
    personal = PORTFOLIO_DATA["personal"]
    buttons = [
        [
            InlineKeyboardButton("🌐 Web Portfolio", url=personal["portfolio"]),
            InlineKeyboardButton("💼 LinkedIn", url=personal["linkedin"])
        ],
        [
            InlineKeyboardButton("🐙 GitHub Profile", url=personal["github"]),
            InlineKeyboardButton("✉️ Email", url=f"mailto:{personal['email']}")
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def get_resume_keyboard() -> InlineKeyboardMarkup:
    """Builds resume access button."""
    personal = PORTFOLIO_DATA["personal"]
    buttons = [
        [InlineKeyboardButton("📄 View / Download Resume", url=personal["portfolio"])]
    ]
    return InlineKeyboardMarkup(buttons)

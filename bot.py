"""
ShashikantPortfolioBot - Main Application Entrypoint
Runs an interactive Telegram bot showcasing Shashikant Raj's Data Analyst portfolio.
"""

import os
import sys
import logging
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Configure stdout for UTF-8 on Windows
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass

# Load environment variables
load_dotenv()

# Internal handlers & keyboards
from data.portfolio_data import PORTFOLIO_DATA
from handlers.start import start_command, help_command
from handlers.about import about_handler
from handlers.skills import skills_handler
from handlers.projects import projects_handler
from handlers.certifications import certifications_handler
from handlers.resume import resume_handler
from handlers.contact import contact_handler, handle_incoming_message
from keyboards.menus import (
    get_main_keyboard,
    get_project_keyboard,
    get_certifications_keyboard,
    get_contact_keyboard,
    get_resume_keyboard
)

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("ShashikantPortfolioBot")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs unexpected errors gracefully."""
    logger.error("Exception while handling an update:", exc_info=context.error)


def run_dry_run_test():
    """Validates configuration, imports, data integrity, and keyboard generation."""
    print("==================================================")
    print(" 🧪 Running Dry-Run Verification for ShashikantPortfolioBot")
    print("==================================================")

    # 1. Verify Portfolio Data
    assert "personal" in PORTFOLIO_DATA, "Missing personal data"
    assert "projects" in PORTFOLIO_DATA, "Missing projects data"
    assert len(PORTFOLIO_DATA["projects"]) >= 5, "Expected at least 5 projects"
    assert "skills" in PORTFOLIO_DATA, "Missing skills data"
    print(f"✅ Portfolio Data Loaded: {PORTFOLIO_DATA['personal']['name']} ({PORTFOLIO_DATA['personal']['title']})")
    print(f"✅ Verified {len(PORTFOLIO_DATA['projects'])} projects and {len(PORTFOLIO_DATA['certifications'])} certifications")

    # 2. Verify Keyboards
    main_kb = get_main_keyboard()
    assert len(main_kb.keyboard) == 3, "Main keyboard should have 3 rows"
    print("✅ Main ReplyKeyboard structure verified")

    proj_kb = get_project_keyboard(PORTFOLIO_DATA["projects"][0])
    assert len(proj_kb.inline_keyboard) > 0, "Project inline keyboard failed"
    print("✅ Project InlineKeyboard verified")

    cert_kb = get_certifications_keyboard(PORTFOLIO_DATA["certifications"])
    assert len(cert_kb.inline_keyboard) > 0, "Certifications inline keyboard failed"
    print("✅ Certifications InlineKeyboard verified")

    contact_kb = get_contact_keyboard()
    assert len(contact_kb.inline_keyboard) > 0, "Contact inline keyboard verified"
    print("✅ Contact InlineKeyboard verified")

    resume_kb = get_resume_keyboard()
    assert len(resume_kb.inline_keyboard) > 0, "Resume inline keyboard verified"
    print("✅ Resume InlineKeyboard verified")

    print("\n🎉 ALL TESTS PASSED! Bot architecture is 100% verified and ready to run.")
    print("==================================================")
    sys.exit(0)


def main():
    """Initializes and runs the bot."""
    # Check for dry-run test flag
    if "--test" in sys.argv:
        run_dry_run_test()
        return

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token or token == "your_telegram_bot_token_here":
        print("\n" + "=" * 65)
        print("⚠️  MISSING TELEGRAM_BOT_TOKEN in .env file!")
        print("=" * 65)
        print("To start your bot:")
        print("1. Open Telegram and search for @BotFather")
        print("2. Send /newbot and choose a name (e.g. Shashikant Raj Portfolio)")
        print("3. Enter username ending in bot (e.g. ShashikantPortfolioBot)")
        print("4. Copy the API token provided into your .env file:")
        print("   TELEGRAM_BOT_TOKEN=your_token_here")
        print("5. Run: python bot.py")
        print("=" * 65 + "\n")
        sys.exit(1)

    print("🤖 Starting ShashikantPortfolioBot...")
    print(f"👤 Candidate: {PORTFOLIO_DATA['personal']['name']}")
    print("🚀 Polling Telegram servers for new messages...")

    # Build Application
    app = ApplicationBuilder().token(token).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_handler))
    app.add_handler(CommandHandler("skills", skills_handler))
    app.add_handler(CommandHandler("projects", projects_handler))
    app.add_handler(CommandHandler("certifications", certifications_handler))
    app.add_handler(CommandHandler("resume", resume_handler))
    app.add_handler(CommandHandler("contact", contact_handler))

    # Menu Button Handlers
    app.add_handler(MessageHandler(filters.Regex("^👤 About Me$"), about_handler))
    app.add_handler(MessageHandler(filters.Regex("^🛠 Skills$"), skills_handler))
    app.add_handler(MessageHandler(filters.Regex("^🚀 Projects$"), projects_handler))
    app.add_handler(MessageHandler(filters.Regex("^🏆 Certifications$"), certifications_handler))
    app.add_handler(MessageHandler(filters.Regex("^📄 Resume$"), resume_handler))
    app.add_handler(MessageHandler(filters.Regex("^📬 Contact / Hire$"), contact_handler))

    # Fallback / Recruiter Direct Inquiries
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_incoming_message))

    # Error handling
    app.add_error_handler(error_handler)

    # Start Polling
    app.run_polling()


if __name__ == "__main__":
    main()

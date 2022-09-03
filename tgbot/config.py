# any configuration should be stored here
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
ADMIN = os.getenv("ADMIN")
ADMIN_USER = os.getenv("ADMIN_USER")
ALERTS_CHANNEL = os.getenv("ALERTS_CHANNEL")

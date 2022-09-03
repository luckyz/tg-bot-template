# filters
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func

# states
from tgbot.states.register_state import Register

# utils
from tgbot.utils.database import Database

# telebot
from telebot import TeleBot, logger
import logging

# config
from tgbot import config

db = Database()

# remove this if you won't use middlewares:
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
bot = TeleBot(config.TELEGRAM_TOKEN, num_threads=5)
logger.setLevel(logging.INFO)

def register_handlers():
    bot.register_message_handler(admin_user, commands=["start"], admin=True, pass_bot=True)
    bot.register_message_handler(any_user, commands=["start"], admin=False, pass_bot=True)
    bot.register_message_handler(anti_spam, commands=["spam"], pass_bot=True)

register_handlers()

# middlewares
bot.register_middleware_handler(antispam_func, update_types=["message"])


# custom filters
bot.add_custom_filter(AdminFilter())

def main():
    print(f"\n[+] Running Telegram Bot (@{config.BOT_USERNAME})...")
    bot.infinity_polling()


if "__main__" == __name__:
    main()

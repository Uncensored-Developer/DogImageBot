from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from dogimagebot.bot import bop
import os


load_dotenv()


def main():
    updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher
    handler = CommandHandler('bop', bop)
    dp.add_handler(handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

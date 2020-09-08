from telegram.ext import CallbackContext
from telegram.update import Update
from .utils import get_image_url


def bop(update: Update, context: CallbackContext):
    url = get_image_url()
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=url)

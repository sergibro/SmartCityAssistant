import modules.utils as utils
from telegram.ext import Filters
from telegram import ParseMode
from modules.parsers.online import OnlineParser

HELP_DICT = {
    "/start": "Start bot.",
    "/get_top_posts interested_terms": "Top posts for UA last day.",
    "/help": "Get help info."
}

def start(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def help(bot, update, args):
    msg = "\n".join([cmd + ' - ' + descr for cmd, descr in HELP_DICT.items()])
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def crash(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="Crashing...")
    utils.time.sleep(1)
    bot.send_message(chat_id=update.message.chat_id, text="Crashed")
    utils.updater.stop()
    utils.updater.is_idle = False

def get_top_posts(bot, update, args):
    # args - that's text from user as array[string]
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text="Looking for tops...")
    op = OnlineParser()
    resList = op.get_top_posts(text_caps)
    links = ["[this is link](" + p["postTelegramUrl"]+ ")" for p in resList]
    msg = "\n".join(links)
    bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)



#def get_trends_stats(bot, update, args):
#     get trends by key
#     using SDao


commands_handlers_dict = {
    "start": start,
    "help": help,
    "get_top_posts": get_top_posts,
    "crash": crash
}

def unknown_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def unknown_all(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, my functionality is quite poor now.")

messages_handlers_dict = {
    Filters.command: unknown_command,
    Filters.all: unknown_all
}

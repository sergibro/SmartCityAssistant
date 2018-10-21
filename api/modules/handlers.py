
HELP_DICT = {
    "/start": "Start bot.",
    "/help": "Get help info.",
}

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

all_handlers = [
    "start": start,
    "help": help,
    "unknown": unknown
]

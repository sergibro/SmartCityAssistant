
HELP_DICT = {
    "/start": "Start bot.",
    "/help": "Get help info.",
}

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def help(bot, update):
    msg = "\n".join([cmd + ' - ' + descr for cmd, descr in HELP_DICT.items()])
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

all_handlers_dict = {
    "start": start,
    "help": help,
    "unknown": unknown
}

import logging.config

from telegram.ext import CommandHandler, MessageHandler

import modules.utils as utils
from modules.handlers import commands_handlers_dict, messages_handlers_dict


if __name__ == '__main__':
    logging.config.dictConfig(utils.config['logging'])

    dispatcher = utils.updater.dispatcher
    for handler_name, handler_func in commands_handlers_dict.items():
        dispatcher.add_handler(CommandHandler(handler_name, handler_func))
    for handler_filter, handler_func in messages_handlers_dict.items():
        dispatcher.add_handler(MessageHandler(handler_filter, handler_func))

    logging.info('Start bot')
    utils.updater.start_polling()

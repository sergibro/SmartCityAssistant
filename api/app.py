import logging
from telegram.ext import Updater, CommandHandler
from modules.handlers import all_handlers_dict

with open('resources/config.json', encoding='utf-8') as f:
    config = json.load(f)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    updater = Updater(token=config.get('TOKEN'))
    dispatcher = updater.dispatcher
    for handler_name, handler_func in all_handlers_dict.items():
        dispatcher.add_handler(CommandHandler(handler_name, handler_func))

    logging.info('Start bot')
    updater.start_polling()

import json
import time
from telegram.ext import Updater

with open('resources/config.json', encoding='utf-8') as f:
    config = json.load(f)

updater = Updater(token=config['TOKEN'])

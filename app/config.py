from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("Ошибка: токен бота не найден в конфигурационном файле")
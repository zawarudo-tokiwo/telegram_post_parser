import os

from pyrogram.client import Client
from pyrogram.errors import exceptions

import settings

API_ID = settings.API_ID
API_HASH = settings.API_HASH


def auth_user(session_name: str) -> Client:  # TODO поменять type hints?
    # Для того, чтобы использовать наш клиент, нужно сначала создать его сессию
    # Если нужная сессия уже существует в файловой системе ("session_name".session) то используется она
    # Иначе создаётся новая сессия
    try:
        client = Client(session_name, api_id=API_ID, api_hash=API_HASH)
        return client
    # Если пользователь завершил свою сессию, например, через телеграмм
    # То нужно пересоздать её
    except exceptions.unauthorized_401.AuthKeyUnregistered:
        os.remove(f"{session_name}.session")
        return auth_user(session_name)
    # Если по какой-то причине нельзя удалить файл сессии, то вызываем исключение
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        raise OSError

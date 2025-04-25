import argparse

from halo import Halo
from pyrogram import filters
from pyrogram.types.messages_and_media import Message

from auth import auth_user
from utils import *


client = auth_user("my_account")


async def main():
    async with client:
        with Halo(text='Fetching chats...'):
            await get_dialogues(client)

        if args.dialogs:
            await show_dialogues(client)  # This thing is slow

        if args.write_dialogs:
            await write_dialogues(client)

        if args.chat_members:
            with Halo(text='Writing chat members...'):
                await write_chat_members(client, args.chat_members)

        if args.chat_history:
            with Halo(text='Saving chat history...'):
                await write_chat_history(client, args.chat_history, args.limit)

        if args.message:
            message = args.message.split(',')
            chat_name = message[0]
            message = message[1]
            await send_message(client, chat_name, message)

if __name__ == "__main__":
    # Парсим аргументы из командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--session",
                        default="my_account", help="Session to use")
    parser.add_argument("-d", "--dialogs", const=True, nargs="?",
                        help="List user's dialogues(chats)")
    parser.add_argument("-wd", "--write_dialogs", const=True, nargs="?",
                        help="Save user's dialogues(chats)")
    parser.add_argument("-p", "--chat_members",
                        help="Chat name to get members from")
    parser.add_argument("-c", "--chat_history",
                        help="Chat name to get history from")
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit of messages in chat history"
    )
    parser.add_argument("-L", "--listen_chat", type=str,
                        help="Chat to get updates from")
    parser.add_argument(
        "-m", "--message", type=str,
        help="Send message to chat (chat_name, text)"
    )
    args = parser.parse_args()

    """
    Если нужно получать сообщения от телеграмма, то нужно добавить к нашему клиенту Update Handler. И запустить его.
    Если клиент запустить до добавления Updete Handler, то он работать не будет.
    """
    if args.listen_chat:
        client.run(main())  # Мы запускаем main от клиента, т.к. нам нужно получить чаты и их индетнтификаторы (заполнить словарь dialogues)

        print(f'Listening "{args.listen_chat}"')

        # Добавляем Updete Handler к нашему клиенту, используя декоратор
        @client.on_message(filters.chat(dialogues[args.listen_chat]))
        async def listen_chat(client: Client, message: Message) -> None:
            """
            Функция вызываемая при получении сообщения из указанного чата.
            Дублирует полученное сообщение в консоль.
            """
            print(message.text)

        client.run()  # Запускаем клиент с добавленным Update Handler

        exit()  # Завершаем работу программы после того, как остановим наш клиент

    # Если нам не надо добавлять Update Handler к клиенту, то просто выполняем нужные функции из main
    client.run(main())

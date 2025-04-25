import json
from typing import Dict

import aiofiles
from pyrogram.client import Client
from pyrogram.session import session

# Сюда сохраняем диалоги пользователя в формате Dialog.chat.name or Dialog.chat.title : Dialog.chat_id. Быстро ничего лучше не придумал
dialogues = {}


async def get_dialogues(client: Client) -> Dict:
    global dialogues

    try:
        async with aiofiles.open(client.name + "_dialogues" + ".json", 'r+') as dialogues_json:

            try:
                dialogues = json.loads(await dialogues_json.read())

            except json.decoder.JSONDecodeError as error:  # If dialogues_json is empty
                async for dialogue in client.get_dialogs():
                    if dialogue.chat.last_name is None:
                        dialogues[dialogue.chat.first_name or dialogue.chat.title] = dialogue.chat.id
                    else:
                        dialogues[dialogue.chat.first_name + " " +
                                  dialogue.chat.last_name] = dialogue.chat.id

                await dialogues_json.write(json.dumps(dialogues))

    except FileNotFoundError:
        # If the file doesn't exist, open it in write mode ('w') to create it
        # then reopen it in read-write mode ('r+')
        async with aiofiles.open(client.name + "_dialogues" + ".json", 'w') as dialogues_json:
            pass
        await get_dialogues(client)

    return dialogues


async def save_dialogues(client: Client) -> None:

    async with aiofiles.open(client.name + "_dialogues" + ".json", mode="w") as f:
        if dialogues:
            json.dump(dialogues, f)
        else:
            json.dump(get_dialogues(client), f)


async def show_dialogues(client: Client) -> None:

    if not (len(dialogues.keys())):
        await get_dialogues(client)

    for dialogue in dialogues.keys():
        print(dialogue)


async def write_chat_members(client: Client, chat_name: str):

    chat_id = dialogues[chat_name]
    async with aiofiles.open(chat_name + " members" + ".json", mode="w") as f:
        async for member in client.get_chat_members(chat_id):
            await f.write(str(member))


async def write_chat_history(client: Client, chat_name: str, limit: int) -> None:

    chat_id = dialogues[chat_name]
    async with aiofiles.open(chat_name + ".json", mode="w") as f:
        async for message in client.get_chat_history(chat_id, limit=limit):
            await f.write(str(message))


async def send_message(client: Client, chat_name: str, message: str) -> None:
    chat_id = dialogues[chat_name]
    await client.send_message(chat_id, f"{message} \n**This message was sent with Pyrogram**!")


# async def write_dialogues(client: Client):
#
#     async with aiofiles.open(client.name + "_dialogues" + ".json", mode="w") as f:
#         async for dialogue in client.get_dialogs():
#             await f.write(str(dialogue))

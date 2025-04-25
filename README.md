uv run main.py --help

usage: main.py [-h] [-s SESSION] [-d [DIALOGS]] [-wd [WRITE_DIALOGS]]
               [-p CHAT_MEMBERS] [-c CHAT_HISTORY] [-l LIMIT] [-L LISTEN_CHAT]
               [-m MESSAGE]

options:
  -h, --help            show this help message and exit
  -s, --session SESSION
                        Session to use
  -d, --dialogs [DIALOGS]
                        List user's dialogues(chats)
  -wd, --write_dialogs [WRITE_DIALOGS]
                        Save user's dialogues(chats)
  -p, --chat_members CHAT_MEMBERS
                        Chat name to get members from
  -c, --chat_history CHAT_HISTORY
                        Chat name to get history from
  -l, --limit LIMIT     Limit of messages in chat history
  -L, --listen_chat LISTEN_CHAT
                        Chat to get updates from
  -m, --message MESSAGE
                        Send message to chat (chat_name, text)

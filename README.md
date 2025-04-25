# Telegram Chat Tool

A Python script to interact with Telegram chats using the `uv` package manager. This tool allows you to manage sessions, list dialogues, retrieve chat members, fetch chat history, listen for updates, and send messages.

## Prerequisites

- Python 3.8+
- `uv` package manager
- Telegram API credentials (set up in your environment or configuration)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

## Usage

Run the script with `uv` and use the available options to interact with Telegram chats.

### Command

```bash
uv run main.py [options]
```

### Options

| Option                       | Description                          |
|------------------------------|--------------------------------------|
| `-h`, `--help`               | Show the help message and exit       |
| `-s`, `--session SESSION`    | Specify the session to use           |
| `-d`, `--dialogs [DIALOGS]`  | List user's dialogues (chats)        |
| `-wd`, `--write_dialogs [WRITE_DIALOGS]` | Save user's dialogues (chats)    |
| `-p`, `--chat_members CHAT_MEMBERS` | Get members from a specific chat |
| `-c`, `--chat_history CHAT_HISTORY` | Get history from a specific chat |
| `-l`, `--limit LIMIT`        | Limit the number of messages in chat history |
| `-L`, `--listen_chat LISTEN_CHAT` | Listen for updates from a chat   |
| `-m`, `--message MESSAGE`    | Send a message to a chat (format: `chat_name,text`) |

### Examples

1. **List all dialogues**:
   ```bash
   uv run main.py --dialogs
   ```

2. **Get chat history with a message limit**:
   ```bash
   uv run main.py --chat_history "MyChat" --limit 50
   ```

3. **Send a message to a chat**:
   ```bash
   uv run main.py --message "MyChat,Hello everyone!"
   ```

4. **Listen for updates from a chat**:
   ```bash
   uv run main.py --listen_chat "MyChat"
   ```

## Notes

- Ensure you have a valid Telegram session configured before running the script.
- The `--message` option expects the chat name and message text in the format `chat_name,text`.

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## License

This project is licensed under the MIT License.

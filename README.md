# TelegramMessage
TelegramMessage is a lightweight Python package designed to simplify the process of sending messages through a Telegram bot.

# Features
* Send text messages via Telegram bot.
* Support for markdown or HTML message formatting.
* Option to disable web page previews in messages.

# Installation
```
git clone https://github.com/kstka/telegram-message
cd telegram-message
pip install .
```

# Usage
```python
from telegram-message import TelegramMessage

bot = TelegramMessage('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')

response = bot.send('Hello, world!')
print(response)

response = bot.send('Hi there!', 'YOUR_OTHER_CHAT_ID')
print(response)
```

# License
MIT


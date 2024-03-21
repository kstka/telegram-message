import requests


class TelegramBotError(Exception):
    """Custom exception for Telegram bot errors."""
    def __init__(self, message):
        super().__init__(message)


class TelegramMessage:
    """
    A class to send messages via a Telegram bot.

    Attributes:
        bot_token (str): The Telegram bot token.
        chat_id (str, optional): Default chat ID for messages.
        parse_mode (str, optional): Formatting option for messages ('markdown' or 'HTML').
        disable_web_page_preview (bool, optional): Disable link previews in messages.

    Methods:
        send: Send text messages.
    """

    def __init__(self, bot_token, chat_id=None, parse_mode='markdown', disable_web_page_preview=False, timeout=10):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
        self.timeout = timeout

    def _send_request(self, method, payload):
        """Internal method to send requests to the Telegram API."""
        api_url = f"https://api.telegram.org/bot{self.bot_token}/{method}"
        try:
            response = requests.post(api_url, data=payload, timeout=self.timeout)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.
            return response.json()  # Returns the response in JSON format.
        except requests.exceptions.RequestException as e:
            raise TelegramBotError(f"Request to Telegram API failed: {e}")

    def send(self, message, chat_id=None):
        """
        Send a text message to a specified chat via Telegram bot.

        Parameters:
            message (str): The message text to send.
            chat_id (str, optional): The chat ID. Overrides the default if provided.

        Returns:
            dict: The response from Telegram API.

        Raises:
            TelegramBotError: If chat ID is not specified or an API request fails.
        """
        if not chat_id and not self.chat_id:
            raise TelegramBotError('Chat ID unknown')

        chat_id = chat_id or self.chat_id  # Use provided chat_id or default to self.chat_id
        params = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': self.parse_mode,
            'disable_web_page_preview': str(self.disable_web_page_preview).lower()
        }

        return self._send_request('sendMessage', params)


# Example Usage
if __name__ == "__main__":
    bot = TelegramMessage('YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')
    try:
        # Sending a text message
        response = bot.send('Hello, world!')
        print(response)
    except TelegramBotError as e:
        print(e)

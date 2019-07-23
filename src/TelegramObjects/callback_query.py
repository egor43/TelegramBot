"""
The class describes the CallbackQuery object from Telegram API
https://tlgrm.ru/docs/bots/api#callbackquery

author: Myshko E.V.
"""


class CallbackQuery():
    """
    This object represents an incoming feedback request from an inline button with a given callback_data.
    """

    id = None
    user = None
    message = None
    inline_message_id = None
    data = None

    def __init__(self, callback_query: dict):
        """
        Object initialization
        :param callback_query: The callback query data that was received from the update object api telegram
        """
        pass
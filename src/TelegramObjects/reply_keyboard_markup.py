"""
The class describes the ReplyKeyboardMarkup object from Telegram API
https://tlgrm.ru/docs/bots/api#replykeyboardmarkup

author: Myshko E.V.
"""


class ReplyKeyboardMarkup:
    """
    This object represents a keyboard with response options.
    """

    keyboard = None
    resize_keyboard = None
    one_time_keyboard = None
    selective = None


    def __init__(self, reply_keyboard_data: dict):
        """
        Object initialization
        :param reply_keyboard_data: The reply keyboard data that was received from the update object api telegram
        """
        pass
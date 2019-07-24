"""
The class describes the InlineKeyboardMarkup object from Telegram API
https://tlgrm.ru/docs/bots/api#inlinekeyboardmarkup

author: Myshko E.V.
"""


class InlineKeyboardMarkup:
    """
    This object represents the built-in keyboard that appears under the corresponding message.
    """

    inline_keyboard = None


    def __init__(self, keyboard_markup_data: dict):
        """
        Object initialization
        :param keyboard_markup_data: The inline keyboard markup data
        """
        pass
"""
The class describes the InlineKeyboardButton object from Telegram API
https://tlgrm.ru/docs/bots/api#inlinekeyboardbutton

author: Myshko E.V.
"""


class InlineKeyboardButton:
    """
    This object represents one button on the integrated keyboard. You must use exactly one optional field.
    """

    text = None
    url = None
    callback_data = None
    switch_inline_query = None
    switch_inline_query_current_chat = None
    callback_game = None


    def __init__(self, keyboard_button_data: dict):
        """
        Object initialization
        :param keyboard_button_data: The inline keyboard button data
        """
        pass
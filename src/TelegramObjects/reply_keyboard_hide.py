"""
The class describes the ReplyKeyboardHide object from Telegram API
https://tlgrm.ru/docs/bots/api#replykeyboardhide

author: Myshko E.V.
"""


class ReplyKeyboardHide:
    """
    After receiving a message with this object, the Telegram application will collapse the bot's
    keyboard and display the device’s standard keyboard (with letters).
    """

    hide_keyboard = None
    selective = None


    def __init__(self, keyboard_hide_data: dict):
        """
        Object initialization
        :param keyboard_hide_data: The keyboard hide data
        """
        pass
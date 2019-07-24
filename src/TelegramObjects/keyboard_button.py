"""
The class describes the KeyboardButton object from Telegram API
https://tlgrm.ru/docs/bots/api#keyboardbutton

author: Myshko E.V.
"""


class KeyboardButton:
    """
    This object represents one button in the answer keyboard.
    For ordinary text buttons, this object can be replaced with a line containing the text on the button.
    """

    text = None
    request_contact = None
    request_location = None


    def __init__(self, keyboard_button_data: dict):
        """
        Object initialization
        :param keyboard_button_data: The keyboard button data
        """
        pass
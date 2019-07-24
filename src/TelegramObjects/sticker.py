"""
The class describes the Sticker object from Telegram API
https://tlgrm.ru/docs/bots/api#sticker

author: Myshko E.V.
"""


class Sticker:
    """
    This object represents a sticker.
    """

    file_id = None
    width = None
    height = None
    thumb = None
    file_size = None


    def __init__(self, sticker_data: dict):
        """
        Object initialization
        :param sticker_data: The sticker data that was received from the update object api telegram
        """
        pass
"""
The class describes the PhotoSize object from Telegram API
https://tlgrm.ru/docs/bots/api#photosize

author: Myshko E.V.
"""


class PhotoSize:
    """
    This object represents an image of a certain size or a preview of a file / sticker.
    """

    file_id = None
    width = None
    height = None
    file_size = None


    def __init__(self, photo_size_data: dict):
        """
        Object initialization
        :param message_entity_data: The photo size data that was received from the update object api telegram
        """
        pass
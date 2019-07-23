"""
The class describes the MessageEntity object from Telegram API
https://tlgrm.ru/docs/bots/api#messageentity

author: Myshko E.V.
"""


class MessageEntity():
    """
    This object represents one of the special entities in the text message.
    For example: hashtags, user names, links, etc.
    """

    type = None
    offset = None
    length = None
    url = None


    def __init__(self, message_entity_data: dict):
        """
        Object initialization
        :param message_entity_data: The message entity data that was received from the update object api telegram
        """
        pass
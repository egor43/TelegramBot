"""
The class describes the Message object from Telegram API
https://tlgrm.ru/docs/bots/api#message

author: Myshko E.V.
"""


class Message():
    """
    Describes the message data from chat update
    """

    message_id = None
    user = None  # The user who sent the message
    date = None
    entities = None
    text = None
    chat = None

    def __init__(self, message_data: dict):
        """
        Object initialization
        :param message_data: The message data that was received from the update object api telegram
        """
        pass
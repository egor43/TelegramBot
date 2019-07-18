"""
The class describes the Message object from Telegram API
https://tlgrm.ru/docs/bots/api#message

author: Myshko E.V.
"""

class Message():
    """
    Describes the message data from chat update
    """

    # Message identifier
    message_id = None
    # The user who sent the message
    user = None
    # Message date
    date = None
    # Message entities
    entities = None
    # Message text
    text = None
    # Chat info
    chat = None

    def __init__(self, message_data: dict):
        """
        Object initialization
        :param message_data: The message data that was received from the update object api telegram
        """
        pass
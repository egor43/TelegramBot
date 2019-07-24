"""
The class describes the Message object from Telegram API
https://tlgrm.ru/docs/bots/api#message

author: Myshko E.V.
"""


class Message:
    """
    This object is a message.
    """

    message_id = None
    user = None
    date = None
    chat = None
    forward_from = None
    forward_date = None
    reply_to_message = None
    text = None
    entities = None
    audio = None
    document = None
    photo = None
    sticker = None
    video = None
    voice = None
    caption = None
    contact = None
    location = None
    venue = None
    new_chat_member = None
    left_chat_member = None
    new_chat_title = None
    new_chat_photo = None
    delete_chat_photo = None
    group_chat_created = None
    supergroup_chat_created = None
    channel_chat_created = None
    migrate_to_chat_id = None
    migrate_from_chat_id = None
    pinned_message = None


    def __init__(self, message_data: dict):
        """
        Object initialization
        :param message_data: The message data that was received from the update object api telegram
        """
        pass
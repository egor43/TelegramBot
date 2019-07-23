"""
The class describes the Chat object from Telegram API
https://tlgrm.ru/docs/bots/api#chat

author: Myshko E.V.
"""


class Chat():
    """
    This object is a chat.
    """

    id = None
    type = None
    title = None
    username = None
    first_name = None
    last_name = None
    all_members_are_administrators = None


    def __init__(self, chat_data: dict):
        """
        Object initialization
        :param chat_data: The chat data that was received from the update object api telegram
        """
        pass
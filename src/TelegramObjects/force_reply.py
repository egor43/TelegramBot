"""
The class describes the ForceReply object from Telegram API
https://tlgrm.ru/docs/bots/api#forcereply

author: Myshko E.V.
"""


class ForceReply:
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user.
    """

    force_reply = None
    selective = None


    def __init__(self, force_reply_data: dict):
        """
        Object initialization
        :param force_reply_data: The force reply data
        """
        pass
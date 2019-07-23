"""
The class describes the Update object from Telegram API
https://tlgrm.ru/docs/bots/api#update

author: Myshko E.V.
"""


class Update():
    """
    This object is an incoming update.
    For example, receiving messages from the user.
    """

    message = None
    update_id = None
    inline_query = None
    chosen_inline_result = None
    callback_query = None

    def __init__(self, update_data: dict):
        """
        Object initialization
        :param update_data: Data received when updating chat from api telegram
        """
        pass
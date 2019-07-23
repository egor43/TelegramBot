"""
The class describes the InlineQuery object from Telegram API
https://tlgrm.ru/docs/bots/api#inlinequery

author: Myshko E.V.
"""


class InlineQuery():
    """
    This object represents an incoming inline query.
    When the user sends an empty query, your bot could return some default or trending results.
    """

    id = None
    user = None
    location = None
    query = None
    offset = None

    def __init__(self, inline_query_data: dict):
        """
        Object initialization
        :param inline_query_data: The inline query data that was received from the update object api telegram
        """
        pass
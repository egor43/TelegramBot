"""
The class describes the ChosenInlineResult object from Telegram API
https://tlgrm.ru/docs/bots/api#choseninlineresult

author: Myshko E.V.
"""


class ChosenInlineResult():
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    """

    result_id = None
    user = None
    location = None
    inline_message_id = None
    query = None

    def __init__(self, chosen_inline_data: dict):
        """
        Object initialization
        :param chosen_inline_data: The chosen inline result data that was received from the update object api telegram
        """
        pass
"""
The class describes the ResponseParameters object from Telegram API
https://tlgrm.ru/docs/bots/api#responseparameters

author: Myshko E.V.
"""


class ResponseParameters:
    """
    Contains information about why the request was not successful.
    """

    migrate_to_chat_id = None
    retry_after = None


    def __init__(self, response_parameters_data: dict):
        """
        Object initialization
        :param force_reply_data: The response parameters data
        """
        pass
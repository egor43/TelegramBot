"""
The class describes the Update object from Telegram API
https://tlgrm.ru/docs/bots/api#update

author: Myshko E.V.
"""


class Update():
    """
    Describes the data from chat update
    """

    # Update message
    message = None
    # Update identifier
    update_id = None


    def __init__(self, update_data: dict):
        """
        Object initialization
        :param update_data: Data received when updating chat from api telegram
        """
        pass
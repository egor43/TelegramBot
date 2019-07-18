"""
The class describes the object Update.
https://tlgrm.ru/docs/bots/api#update

author: Myshko E.V.
"""

import json

class Update():
    """
    Describes the data received when updating the chat
    """

    # Update message
    message = None
    # Update identifier
    update_id = None


    def __init__(self, telegram_request_data: bytes):
        """
        Object initialization
        :param telegram_request_data: Data received when updating chat from api telegram
        """
        dict_data = json.loads(telegram_request_data.decode())
        pass
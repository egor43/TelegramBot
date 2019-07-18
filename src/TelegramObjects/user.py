"""
The class describes the User object from Telegram API
https://tlgrm.ru/docs/bots/api#message

author: Myshko E.V.
"""


class User():
    """
    Describes the user data from chat update
    """

    user_id = None
    username = None
    first_name = None
    last_name = None
    is_bot = None
    language_code = None

    def __init__(self, user_data: dict):
        """
        Object initialization
        :param user_data: The user data that was received from the update object api telegram
        """
        pass
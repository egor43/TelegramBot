"""
The class describes the User object from Telegram API
https://tlgrm.ru/docs/bots/api#user

author: Myshko E.V.
"""


class User():
    """
    This object represents a bot or Telegram user.
    """

    id = None
    first_name = None
    first_name = None
    last_name = None
    username = None


    def __init__(self, user_data: dict):
        """
        Object initialization
        :param user_data: The user data that was received from the update object api telegram
        """
        pass
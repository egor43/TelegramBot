"""
The class describes the Contact object from Telegram API
https://tlgrm.ru/docs/bots/api#contact

author: Myshko E.V.
"""


class Contact:
    """
    This object represents a contact with a phone number.
    """

    phone_number = None
    first_name = None
    last_name = None
    user_id = None


    def __init__(self, contact_data: dict):
        """
        Object initialization
        :param contact_data: The contact data that was received from the update object api telegram
        """
        pass
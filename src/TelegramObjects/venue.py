"""
The class describes the Venue object from Telegram API
https://tlgrm.ru/docs/bots/api#venue

author: Myshko E.V.
"""


class Venue:
    """
    This object represents the object on the map.
    """

    location = None
    title = None
    address = None
    foursquare_id = None


    def __init__(self, venue_data: dict):
        """
        Object initialization
        :param venue_data: The venue data that was received from the update object api telegram
        """
        pass
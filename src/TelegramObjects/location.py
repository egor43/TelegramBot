"""
The class describes the Location object from Telegram API
https://tlgrm.ru/docs/bots/api#location

author: Myshko E.V.
"""


class Location:
    """
    This object represents a point on the map.
    """

    longitude = None
    latitude = None


    def __init__(self, location_data: dict):
        """
        Object initialization
        :param location_data: The location data that was received from the update object api telegram
        """
        pass
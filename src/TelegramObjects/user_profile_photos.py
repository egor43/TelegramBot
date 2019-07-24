"""
The class describes the UserProfilePhotos object from Telegram API
https://tlgrm.ru/docs/bots/api#userprofilephotos

author: Myshko E.V.
"""


class UserProfilePhotos:
    """
    This object contains user profile pictures.
    """

    total_count = None
    photos = None


    def __init__(self, profile_photos_data: dict):
        """
        Object initialization
        :param profile_photos_data: The profile photos data that was received from the update object api telegram
        """
        pass
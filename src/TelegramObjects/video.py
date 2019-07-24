"""
The class describes the Video object from Telegram API
https://tlgrm.ru/docs/bots/api#video

author: Myshko E.V.
"""


class Video:
    """
    This object represents a video.
    """

    file_id = None
    width = None
    height = None
    duration = None
    thumb = None
    mime_type = None
    file_size = None


    def __init__(self, video_data: dict):
        """
        Object initialization
        :param video_data: The video data that was received from the update object api telegram
        """
        pass
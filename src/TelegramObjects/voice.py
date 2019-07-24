"""
The class describes the Voice object from Telegram API
https://tlgrm.ru/docs/bots/api#voice

author: Myshko E.V.
"""


class Voice:
    """
    This object represents a voice message.
    """

    file_id = None
    duration = None
    mime_type = None
    file_size = None


    def __init__(self, voice_data: dict):
        """
        Object initialization
        :param voice_data: The voice data that was received from the update object api telegram
        """
        pass
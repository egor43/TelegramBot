"""
The class describes the Audio object from Telegram API
https://tlgrm.ru/docs/bots/api#audio

author: Myshko E.V.
"""


class Audio:
    """
    This object represents an audio recording that Telegram customers pick up as a music track.
    """

    file_id = None
    duration = None
    performer = None
    title = None
    mime_type = None
    file_size = None


    def __init__(self, audio_data: dict):
        """
        Object initialization
        :param message_entity_data: The audio data that was received from the update object api telegram
        """
        pass
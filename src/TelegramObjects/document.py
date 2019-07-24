"""
The class describes the Document object from Telegram API
https://tlgrm.ru/docs/bots/api#document

author: Myshko E.V.
"""


class Document:
    """
    This object represents a file that is not a photo, voice message, or audio.
    """

    file_id = None
    thumb = None
    file_name = None
    mime_type = None
    file_size = None


    def __init__(self, document_data: dict):
        """
        Object initialization
        :param message_entity_data: The document data that was received from the update object api telegram
        """
        pass
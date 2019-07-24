"""
The class describes the File object from Telegram API
https://tlgrm.ru/docs/bots/api#file

author: Myshko E.V.
"""


class File:
    """
    This object represents a file ready for download.
    It can be downloaded from the link like https://api.telegram.org/file/bot <token> / <file_path>.
    The link will be valid for at least 1 hour.
    After this period, it can be requested again using the getFile method.
    """

    file_id = None
    file_size = None
    file_path = None


    def __init__(self, file_data: dict):
        """
        Object initialization
        :param file_data: The file data that was received from the update object api telegram
        """
        pass
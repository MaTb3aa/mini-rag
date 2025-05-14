from fastapi import UploadFile
from controllers.BaseController import BaseController
from models import ResponseSignal
class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_file(self,file: UploadFile):
        """
        Validate the file type and size.
        """
        allowed_extensions = self.app_settings.ALLOWED_EXTENSIONS
        max_file_size = self.app_settings.MAX_FILE_SIZE

        if file.content_type not in allowed_extensions:
            return False, ResponseSignal.FILE_TYPE_NOT_ALLOWED

        if file.size > max_file_size:
            return False, ResponseSignal.FILE_SIZE_EXCEEDS_LIMIT


        return True, ResponseSignal.FILE_UPLOADED
from fastapi import UploadFile
from controllers.BaseController import BaseController
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os
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

    def generate_unique_path(self, filename: str,project_id: str) -> str:
        """
        Generate a unique filename for the uploaded file.
        """

        unique_random_key = self.generate_random_string()
        project_path = ProjectController().get_project_dir(project_id=project_id)
        
        clean_filename = self.get_clean_file_name(filename=filename)
        new_file_path = os.path.join(project_path, f"{unique_random_key}_{clean_filename}")

        while os.path.exists(new_file_path):
            unique_random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path, f"{unique_random_key}_{clean_filename}")

        return new_file_path, unique_random_key + "_" + clean_filename
    
    def get_clean_file_name(self, filename: str) -> str:
        """
        Get a clean file name by removing special characters.
        """
        clean_filename = re.sub(r'[^\w]', '', filename.strip())

        clean_filename = clean_filename.replace(" ", "_")
        return clean_filename
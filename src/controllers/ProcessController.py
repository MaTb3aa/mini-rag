from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loader import PyMuPDFLoader
from models import ProcessingEnum
class ProcessController(BaseController):
    def __init__(self, project_id : str):
        super().__init__()
        self.project_id = project_id
        self.project_controller = ProjectController()
        self.project_path = self.project_controller.get_project_dir(project_id=self.project_id)

    def get_file_exists(self, file_id: str) -> bool:
        """
        Check if the file exists in the project directory.
        """
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str, file_path : str):
        """
        Get the appropriate file loader based on the file extension.
        """
        file_extension = self.get_file_exists(self)
        if file_extension == ProcessingEnum.TXT:
            return TextLoader(file_path, encoding="utf-8")
        elif file_extension == ProcessingEnum.PDF:
            return PyMuPDFLoader(file_path, encoding="utf-8")
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
       
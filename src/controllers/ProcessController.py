from .BaseController import BaseController
from .ProjectController import ProjectController
import os
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
       
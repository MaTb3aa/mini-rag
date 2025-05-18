from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from models import ProcessingEnum
class ProcessController(BaseController):
    def __init__(self, project_id : str):
        super().__init__()
        self.project_id = project_id
        self.project_controller = ProjectController()
        self.project_path = self.project_controller.get_project_dir(project_id=self.project_id)

    def get_file_extension(self, file_id: str) -> str:
        ext = os.path.splitext(file_id)[1].lower()
        if not ext:
            raise ValueError(f"File '{file_id}' does not have an extension.")
        return ext

    def get_file_loader(self, file_id: str):
        """
        Get the appropriate file loader based on the file extension.
        """
        file_extension = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(self.project_path, file_id)

        if file_extension == '.txt':
            return TextLoader(file_path, encoding="utf-8")
        elif file_extension == '.pdf':
            return PyMuPDFLoader(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
    
    def get_file_content(self, file_id: str):
        """
        Get the content of the file using the appropriate loader.
        """
        loader = self.get_file_loader(file_id=file_id)
        documents = loader.load()
        return documents

    def process_file_conteent(self, file_content: list,file_id : str, chunk_size: int = 100, overlap_size: int = 20):
        """
        Process the file content and split it into chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
        )

        file_content_texts = [
            record.page_content
            for record in file_content
        ]
        file_content_metadata = [
            record.metadata
            for record in file_content
        ]
        chunks = text_splitter.create_documents(
            file_content_texts,
            metadatas = file_content_metadata
        )
        return chunks
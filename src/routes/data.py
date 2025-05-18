from fastapi import APIRouter, Depends, UploadFile , status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
import os
from controllers import ProjectController, DataController, ProcessController
from models import ResponseSignal
import aiofiles
import logging
from .schemes.data import ProcessRequest

logger = logging.getLogger('uvicorn.error')

fastapi_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1-data'],
)

@fastapi_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file : UploadFile, app_settings: Settings = Depends(get_settings)):
    """
    Upload data to the project.
    """
   

    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": f"File validation failed: {result_signal}",
                "project_id": project_id,
            },
        )
    
    project_dir = ProjectController().get_project_dir(project_id=project_id)
    file_path,file_id = data_controller.generate_unique_path(filename=file.filename, project_id=project_id)


    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "signal": ResponseSignal.FILE_NOT_SAVED.value,
            },
        )
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": f"File uploaded successfully: {result_signal}",
            "project_id": project_id,
            "file_path": project_dir,
            "signal": ResponseSignal.FILE_SAVED.value,
            "file_id": file_id,
        },

    )

@fastapi_router.post("/process/{project_id}")
async def process_endpoint(project_id: str, request: ProcessRequest, app_settings: Settings = Depends(get_settings)):
    """
    Process data in the project.
    """
    process_controller = ProcessController(project_id=project_id)

    file_id = request.file_id
    chunk_size = request.chunk_size
    overlap_size = request.overlap_size

    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks = process_controller.process_file_conteent(
        file_content=file_content,
        file_id = file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size,
    )
    
    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,    
            content={
                "signal": ResponseSignal.PROCESSING_FAILED
            }
        )

    return file_chunks
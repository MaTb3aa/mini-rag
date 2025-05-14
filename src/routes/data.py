from fastapi import APIRouter, Depends, UploadFile , status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
fastapi_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1-data'],
)

@fastapi_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file : UploadFile, app_settings: Settings = Depends(get_settings)):
    """
    Upload data to the project.
    """
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    app_author = app_settings.APP_AUTHOR
    app_author_email = app_settings.APP_AUTHOR_EMAIL
    app_description = app_settings.APP_DESCRIPTION

    is_valid, result_signal = DataController().validate_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": f"File validation failed: {result_signal}",
                "project_id": project_id,
            },
        )
    
    project_dir = ProjectController().get_project_dir(project_id=project_id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": f"File uploaded successfully: {result_signal}",
            "project_id": project_id,
             "file_path": project_dir,
            
        },

    )
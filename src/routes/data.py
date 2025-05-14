from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController
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
        return {
            "message": "File validation failed",
            "status": "error",
            "signal": result_signal,
        }
    return {
        "message": f"Upload data to {app_name} API",
        "version": app_version,
        "author": app_author,
        "author_email": app_author_email,
        "description": app_description,
        "project_id": project_id,
        "signal": result_signal,
    }
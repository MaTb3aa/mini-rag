from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

fastapi_router = APIRouter(
    prefix='/api/v1/data',
    tags=['api-v1-data'],
)

@fastapi_router.get("/")
async def message(app_settings: Settings =Depends(get_settings)):
    """
    Welcome message for the API."""
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    app_author = app_settings.APP_AUTHOR
    app_author_email = app_settings.APP_AUTHOR_EMAIL
    app_description = app_settings.APP_DESCRIPTION
    return {
        "message": f"Welcome to {app_name} API",
        "version": app_version,
        "author": app_author,
        "author_email": app_author_email,
        "description": app_description,
    }

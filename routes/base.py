from fastapi import APIRouter
import os
fastapi_router = APIRouter(
    prefix='/mini-rag/v1',
    tags=['mini-rag'],
)

@fastapi_router.get("/")
async def message():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": f"Welcome to {app_name} API",
        "version": app_version
    }

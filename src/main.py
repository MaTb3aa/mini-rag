from fastapi import FastAPI
from dotenv import load_dotenv
from routes.base import fastapi_router

app = FastAPI()
app.include_router(fastapi_router)

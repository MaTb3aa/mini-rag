from fastapi import FastAPI
from routes import base_router
from routes import data_router

app = FastAPI()
app.include_router(base_router)
app.include_router(data_router)

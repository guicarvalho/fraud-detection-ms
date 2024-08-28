from fastapi import FastAPI

from src.controllers import router

app = FastAPI()
app.include_router(router)

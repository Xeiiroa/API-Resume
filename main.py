from fastapi import FastAPI
from setup import router

app = FastAPI()
app.include_router(router)
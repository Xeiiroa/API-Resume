from flask import Flask
from dotenv import load_dotenv
from os import path
from fastapi import FastAPI



load_dotenv('.env')

def create_api():
    app = FastAPI()

    from routes import router
    
    app.include_router(router)
    
    return app
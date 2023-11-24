from flask import Flask
from dotenv import load_dotenv
from os import path

load_dotenv('.env')

def create_api():
    global api 
    api=Flask(__name__, template_folder=os.getenv('TEMPLATE_FOLDER_FILEPATH'))
    global api
    
    from .routes import routes
    
    api.register_blueprint(routes, url_prefix="/")
    
    return api
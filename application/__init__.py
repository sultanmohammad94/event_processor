from flask import Flask
from application import settings

def create_app():
    app = Flask(__name__)
    app.name = settings.APP_NAME
    return app
    
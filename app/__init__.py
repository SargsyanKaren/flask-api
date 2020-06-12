import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app: Flask = Flask(__name__)

    CORS(app)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return f'{app.config.get("SECRET_KEY")}'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello'

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app = create_app()
    app.run(host = '0.0.0.0', port=port)
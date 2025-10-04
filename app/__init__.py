from flask import Flask
from .routes import main
def create_app(config = None):
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.register_blueprint(main)
    
    return app
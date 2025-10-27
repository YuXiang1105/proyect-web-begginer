from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config = DevConfig):
    #We create the app
    app = Flask(__name__)
    #we put the desired config to the ap
    app.config.from_object(config)
    #we connect the database to the app
    db.init_app(app)
    from .routes import main
    app.register_blueprint(main)
    return app
from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()
#if the user tries to go to a page that requires login, it redirects to the login page
login_manager.login_view = "auth.login"


def create_app(config = DevConfig):
    #We create the app
    app = Flask(__name__)
    #we put the desired config to the ap
    app.config.from_object(config)

    #we connect the database to the app
    db.init_app(app)
    #we import the blueprints into the app
    from .routes import main
    from .routes import register_blueprint 
    app.register_blueprint(main)  
    app.register_blueprint(register_blueprint)
    
    return app
from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()
#if the user tries to go to a page that requires login, it redirects to the login page
login_manager.login_view = "auth.log_in"


def create_app(config = DevConfig):
    #We create the app
    app = Flask(__name__)
    #we put the desired config to the ap
    app.config.from_object(config)
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)
    #we connect the database to the app
    db.init_app(app)
    #we import the blueprints into the app
    from .routes import main
    from .auth.auth import auth as authentication 
    from .admin.admin import administrator
    app.register_blueprint(main)  
    app.register_blueprint(authentication)
    app.register_blueprint(administrator)
    with app.app_context():
        db.create_all()
    return app
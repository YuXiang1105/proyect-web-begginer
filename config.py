import os 

mydir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'the super secret ket'
    SQLALCHEMY = False
    ALIENS_PER_PAGE = 20
    IMG_FOLDERS = os.path.join(mydir, "app", "static", "user_images") #storage the images in the static folder, in a new folder
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aliens.db'
    DEBUG = True
    ALIENS_PER_PAGE = 6
    IMG_FOLDERS = os.path.join(mydir, "app", "static", "user_images") #storage the images in the static folder, in a new folder

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    WTF_CSRF_ENABLED = False
    ALIENS_PER_PAGE = 6
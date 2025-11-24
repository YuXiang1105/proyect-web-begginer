class Config():
    SECRET_KEY = 'the super secret ket'
    SQLALCHEMY = False
    ALIENS_PER_PAGE = 20
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aliens.db'
    DEBUG = True
    ALIENS_PER_PAGE = 6

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    WTF_CSRF_ENABLED = False
    ALIENS_PER_PAGE = 6
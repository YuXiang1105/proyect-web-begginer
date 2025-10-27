class Config():
    SECRET_KEY = 'the super secret ket'
    SQLALCHEMY = False
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aliens.db'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    WTF_CSRF_ENABLED = False
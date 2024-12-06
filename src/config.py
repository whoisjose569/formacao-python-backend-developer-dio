import os

class Config:
    TESTING = False
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    SECRET_KEY='dev'
    SQLALCHEMY_DATABASE_URI='sqlite:///dio_blog.sqlite'
    JWT_SECRET_KEY = "super-secret"

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "test"
    DATABASE_URL = "sqlite://"
    JWT_SECRET_KEY = "test"
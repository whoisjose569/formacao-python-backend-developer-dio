import os

from flask import Flask
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src.models.base import db

migrate = Migrate()
jwt = JWTManager()


def create_app(environment=os.getenv("ENVIRONMENT", "development")):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f"src.config.{environment.title()}Config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    from src.controllers import user
    from src.controllers import auth
    
    app.register_blueprint(user.bp)
    app.register_blueprint(auth.bp)
    
    return app
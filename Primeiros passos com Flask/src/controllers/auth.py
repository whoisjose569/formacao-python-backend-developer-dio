from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import create_access_token


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return ({"msg": "Bad username or password"}), HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=username)
    return {"access_token": access_token}
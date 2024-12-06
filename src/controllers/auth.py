from flask import Blueprint, request
from src.models.base import db
from src.models.user import User
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from src.app import bcrypt


bp = Blueprint('auth', __name__, url_prefix="/auth")

def _check_password(password_hash, password_raw):
    return bcrypt.check_password_hash(password_hash, password_raw)
    

@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = db.session.query(User).filter_by(username=username).first()
    
    if not user or not _check_password(user.password, password):
        return ({"msg": "Bad username or password"}), HTTPStatus.UNAUTHORIZED
    
    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token}
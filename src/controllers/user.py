from flask import Blueprint, request
from src.models.base import db
from src.models.user import User
from src.models.role import Role
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required
from src.utils import requires_roles
from src.app import bcrypt
from src.views.user import UserSchema, CreateUserSchema
from marshmallow import ValidationError

bp = Blueprint('user', __name__, url_prefix="/users")


def _create_user():
    user_schema = CreateUserSchema()
    try:
        data = user_schema.load(request.json)
    except ValidationError as exception:
        return exception.messages, HTTPStatus.UNPROCESSABLE_ENTITY
    user = User(username=data['username'], password=bcrypt.generate_password_hash(data['password']), role_id=data['role_id'])
    
    db.session.add(user)
    db.session.commit()
    return {'msg': 'User created!'}, HTTPStatus.CREATED

def _create_role():
    data = request.json
    role = Role(name = data["name"])
    
    db.session.add(role)
    db.session.commit()

@jwt_required()
@requires_roles('admin')
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    users_schema = UserSchema(many=True)
    return users_schema.dump(users)

@bp.route('/', methods=["GET", "POST"])
def handle_users():
    if request.method == 'POST':
        return _create_user()
    else:
        return {"users": _list_users()}

@bp.route('/create_role', methods=["POST"])
def create_role():
    _create_role()
    return {"msg": "Role created!"}, HTTPStatus.CREATED

@bp.route('/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id, 
        "username": user.username
    }

@bp.route('/<int:user_id>', methods=["PATCH"])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json
 
    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    
    db.session.commit()
        
    return {
        "id": user.id, 
        "username": user.username
    }

@bp.route('/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    
    db.session.delete(user)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
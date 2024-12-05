from flask_jwt_extended import get_jwt_identity
from src.models.base import db
from src.models.user import User
from functools import wraps
from http import HTTPStatus

def requires_roles(role_name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_id = get_jwt_identity()
            user = db.get_or_404(User, int(user_id))

            if user.role.name != role_name:
                return {"msg": "User dont have access."}, HTTPStatus.UNAUTHORIZED
            return f(*args, **kwargs)
        return wrapped
    return decorator

def eleva_quadrado(x):
    return x**2
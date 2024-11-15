from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus

bp = Blueprint('user', __name__, url_prefix="/users")


def _create_user():
    data = request.json
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {"id": user.id, "username": user.username} for user in users
    ]

@bp.route('/', methods=["GET", "POST"])
def handle_users():
    if request.method == 'POST':
        _create_user()
        return {'message': 'User created!'}, HTTPStatus.CREATED
    else:
        return {"users": _list_users()}

@bp.route('/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id, 
        "username": user.username
    }
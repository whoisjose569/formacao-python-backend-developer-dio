from src.app import ma
from src.views.role import RoleSchema
from marshmallow import fields
from src.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        exclude = ("password","role_id",)
    role = ma.Nested(RoleSchema)

class CreateUserSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)

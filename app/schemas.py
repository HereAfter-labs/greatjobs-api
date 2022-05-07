from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from .models import User
from .app import app

ma = Marshmallow(app)

class loginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(ma.ModelSchema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    email = fields.Email(required=True)
    affiliation = fields.String(required=False)
    password = fields.String(required=True, load_only=True)
    # confirmPassword = fields.String(required=True, load_only=True)

    class Meta:
        model = User
        # exclude = ('analysis', )
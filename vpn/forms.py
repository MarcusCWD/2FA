from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, Optional, ValidationError
from vpn import db
from vpn.models import User

class LoginForm(FlaskForm):

    email = StringField(
        label='Email:',
        validators=[
            Email("Invalid Email"),
            DataRequired(message="Email required")
        ]
    )
    OTP = PasswordField(
        label='OTP:',
        validators=[
            Length(min=6, max=6, message="OTP code must contain 6 digit"),
            DataRequired(message="OTP code required")
        ]
    )
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, Optional, ValidationError
from vpn import db
from vpn.models import User

class LoginForm(FlaskForm):

    def validate_email(self, email_to_check):
        user_dbaccess = db.query(User).filter_by(email_address=email_to_check.data).first()
        db.close()
        if not user_dbaccess:
            raise ValidationError('Invalid Email')

    email = StringField(
        label='Email Address',
        validators=[
            Email("Invalid Email"),
            DataRequired(message="Email required")
        ]
    )
    otp = PasswordField(
        label='OTP Code',
        validators=[
            Length(min=6, max=8, message="OTP Code must contain 6 digit"),
            DataRequired(message="OTP required")
        ]
    )
    login = SubmitField(label='Login')


class RegisterForm(FlaskForm):

    def validate_email(self, email_to_check):
        user_dbaccess = db.query(User).filter_by(email_address=email_to_check.data).first()
        db.close()
        if not user_dbaccess:
            raise ValidationError('Invalid Email')
    email = StringField(
        label='Email Address',
        validators=[
            Email("Invalid Email"),
            DataRequired(message="Email required")
        ]
    )
    epin = PasswordField(
        label='epin',
        validators=[
            Length(min=8, max=8, message="Epin must contain 8 characters"),
            DataRequired(message="Epin required")
        ]
    )
    generate = SubmitField(label='Generate QR')
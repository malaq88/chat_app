# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user
from datetime import datetime

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RoomForm(FlaskForm):
    name = StringField('Room Name', validators=[DataRequired(), Length(min=2, max=50)])
    theme = StringField('Theme', validators=[DataRequired(), Length(min=2, max=50)])
    start_time = DateTimeField('Start Time (YYYY-MM-DD HH:MM:SS)', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    end_time = DateTimeField('End Time (YYYY-MM-DD HH:MM:SS)', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Create Room')

    def validate_end_time(self, end_time):
        if end_time.data <= datetime.utcnow():
            raise ValidationError('End time must be in the future.')

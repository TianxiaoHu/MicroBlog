from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, StringField, TextAreaField
from wtforms.validators import Required, DataRequired, Length

class LoginForm(FlaskForm):
    email = TextField('email', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

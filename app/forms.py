from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    email = TextField('email', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

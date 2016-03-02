from flask.ext.wtf import Form
from wtforms.fields import TextField,SubmitField,RadioField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required,InputRequired ,NumberRange, ValidationError
from flask_wtf.html5 import IntegerField
from sqlalchemy.sql import exists
from app import db
from app.models import User



# def validate_age(form , field):
#     try:
#         age = int(field.data)
#         if not age in range(5,105):
#             field.errors.append('Age is does not fall within valid range')
#             return False
#         return True
#     except TypeError:
#         field.errors.append('Age must be an integer!')
#         return False
        


class LoginForm(Form):
    first_name = TextField('First Name', validators = [Required()])
    last_name = TextField('Last Name', validators = [Required()])
    user_name = TextField('Username' , validators=[Required()])
    age = TextField('Age', validators = [Required(),NumberRange(min=5, max=105)])
    sex = RadioField('Sex', validators = [Required()], choices = [('male', 'Male'),('female', 'Female')])
    img_file = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Jpg or Png Images only!')])
    submit = SubmitField('Submit')


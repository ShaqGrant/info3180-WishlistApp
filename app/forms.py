from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField, FileField, IntegerField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired, Required, Allowed, FileRequired, FileAllowed
from app import db
from app.models import User_profile


def validate_age(form , field):
    try:
        age = int(field.data)
        if not age in range(5,105):
            field.errors.append('Age is does not fall within valid range')
            return False
        return True
    except TypeError:
        field.errors.append('Age must be an integer!')
        return False
        


class LoginForm(Form):
    first_name = TextField('First Name', validators = [Required()])
    last_name = TextField('Last Name', validators = [Required()])
    user_name = TextField('Username' , validators=[Required()])
    age = TextField('Age', validators = [validate_age, Required()])
    sex = SelectField('Sex', validators = [Required()], choices = [('male', 'Male'),('female', 'Female')])
    img_file = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Jpg or Png Images only!')])
    submit = SubmitField('Submit')


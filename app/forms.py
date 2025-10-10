from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, EmailField
from wtforms.validators import DataRequired, Email

class newClass(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     class_imput = StringField('class', validators=[DataRequired()])
     origin = StringField('origin')
     danger = StringField('danger', validators=[DataRequired()])
     description = TextAreaField('description', validators=[DataRequired()])
     submit = SubmitField('submit')
     
class log_in_form(FlaskForm):
     user = StringField('user', validators=[DataRequired()])
     email = EmailField('email', validators=[DataRequired(), Email()])
     password = StringField("password" ,validators=[DataRequired()])
     submit = SubmitField('submit')
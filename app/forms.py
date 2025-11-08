from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
#form to add a new alien to the species page
class newClass(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     class_imput = StringField('class', validators=[DataRequired()])
     origin = StringField('origin')
     danger = StringField('danger', validators=[DataRequired()])
     description = TextAreaField('description', validators=[DataRequired()])
     submit = SubmitField('submit')
     
     #form for the log in
class log_in_form(FlaskForm):
     user = StringField('user', validators=[DataRequired()])
     email = EmailField('email', validators=[DataRequired(), Email()])
     password = PasswordField("password" ,validators=[DataRequired()])
     submit = SubmitField('submit')
     
class register_form(FlaskForm):
     user = StringField('user', validators=[DataRequired()])
     email = EmailField('email', validators=[DataRequired(), Email()])
     password = PasswordField("password" ,validators=[DataRequired(), Length(min=6)])
     password2 = PasswordField("confirm password" ,validators=[DataRequired(),EqualTo('password', message= "password not equal"), ], )
     submit = SubmitField('submit')
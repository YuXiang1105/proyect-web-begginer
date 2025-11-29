from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField,SelectMultipleField,widgets, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User 
 
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
     
     def validate_username(self, username):
          user = User.query.filter_by(username=username.data).first()
          if user is not None:
               raise ValidationError('Please use a different username.')
 
     def validate_email(self, email):
       user = User.query.filter_by(email=email.data).first()
       if user is not None:
          raise ValidationError('Please use a different email address.')

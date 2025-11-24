from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField,SelectMultipleField,widgets, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_wtf.file import FileAllowed
from app.models import User

#form for adding a new alien
class newClass(FlaskForm):
     #It is not necessary to upload an image for a new relic
    image = FileField('image', validators=[FileAllowed(["jpg", "jpeg", "png", "gif"], "invalid file type")])
    name = StringField('Name', validators=[DataRequired()])
    danger = StringField('Danger', validators=[DataRequired()])
    origin = StringField('Origin')
    description = TextAreaField('Description', validators=[DataRequired()])
    class_imput = SelectMultipleField(
        "Classes",
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget()
    )
    submit = SubmitField('Submit')

     
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
     
class editRelicForm(FlaskForm):
     #no data required because the user might not want to change all the fields
    name = StringField('Name')
    image = FileField('image', validators=[FileAllowed(["jpg", "jpeg", "png", "gif"], "invalid file type")])
    danger = StringField('Danger')
    origin = StringField('Origin')
    description = TextAreaField('Description')
    submit = SubmitField('Submit')
    class_imput = SelectMultipleField(
        "Classes",
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget()
    )
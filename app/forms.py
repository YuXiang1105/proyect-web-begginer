from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     class_imput = StringField('class', validators=[DataRequired()])
     origin = StringField('origin')
     danger = StringField('danger', validators=[DataRequired()])
     description = TextAreaField('description', validators=[DataRequired()])
     submit = SubmitField('submit')

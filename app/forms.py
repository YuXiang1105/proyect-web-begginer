from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
     name = StringField('name', validators=[DataRequired()])
     class_imput = StringField('class', validators=[DataRequired()])
     origin = StringField('origin', validators=[DataRequired()])
     danger = StringField('danger', validators=[DataRequired()])
     description = StringField('description', validators=[DataRequired()])
     submit = SubmitField('submit')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectMultipleField,widgets, FileField
from flask_wtf.file import FileAllowed


from wtforms import StringField,  SubmitField, TextAreaField,SelectMultipleField,widgets, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

 
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
    
#form for adding a new alien
class newClassAlien(FlaskForm):
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
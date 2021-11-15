from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    search = StringField('Search', validators=[(DataRequired())])
    count = IntegerField('Number of Products', validators=[(DataRequired())])
    submit = SubmitField('submit')

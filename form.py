from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class ReviewForm(FlaskForm):
    review = StringField('')
    submit = SubmitField('Submit')
from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json
from form import ReviewForm

pipeline = joblib.load('C:/Users/Aman Srivastava/Downloads/pipeline.sav')
app = Flask(__name__)
app.config['SECRET_KEY'] ='Aman'
@app.route('/',methods=['GET','POST'])
def get_delay():
    form = ReviewForm()
    if form.validate_on_submit():
        reviews = form.review.data
        reviews = remove_punctuation_stopwords_lemma(reviews)
        reviews = reviews.strip()
        if len(reviews)==0:
            return '<h1> empty string passed'

        else:
            pred = pipeline.predict([reviews])
            if pred[0]==1:
                return '<h1> Your review is:  {}.' .format('positive')
            elif pred[0]==0:
                return '<h1> Your review is:  {}.'.format('negative')

    return render_template('review.html', form = form)
if __name__ == '__main__':
    app.run(port=8080, debug=True)
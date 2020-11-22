import nltk
import re
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
from nltk.corpus import stopwords


def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer=WordNetLemmatizer()
    stop_words = stopwords.words('english')
    sentence = re.sub(r'[^\w\s]','',sentence)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
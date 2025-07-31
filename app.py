import nltk
from nltk.corpus import stopwords
import json
import random
import numpy as np
from nltk.stem import WordNetLemmatizer
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, session
from flask_mysqldb import MySQL
from MySQLdb import IntegrityError
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spellchecker import SpellChecker
from flask_cors import CORS
from googletrans import Translator

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'random'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sam@2003'
app.config['MYSQL_DB'] = 'login'
mysql = MySQL(app)

# Initialize NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
spell = SpellChecker()

# Load chatbot intents
with open('intents.json') as file:
    intents_data = json.load(file)

# Preprocess text
ignore_words = ['?', '!', '.', ',']
corpus = []
tags = []

# Predefined words dictionary for Kannada and Telugu to English translation
predefined_words = {
    'kn': {
        'ಕಾಲೇಜು': 'college',
        'ಹಾಸ್ಟೆಲ್': 'hostel',
        'ಶಿಕ್ಷಣ': 'education',
        'ಶುಲ್ಕ': 'fees',
        'ಸಂಪರ್ಕಿಸಿ': 'contact',
        'ಸಾರಿಗೆ':'transport',
        'ಸ್ಥಾಪಕ':'founder',
        'ಸಂಶೋಧನೆ':'research',
        'ಕ್ರೀಡೆ':'sports',
        'ರಜೆ':'vacation',
        'ವಿದ್ಯಾರ್ಥಿವೇತನ':'scholorship',
        'ಪ್ರಾಂಶುಪಾಲರು':'principal',
        'ಗ್ರಂಥಾಲಯ':'library',
        'ಸಿಲಬಸ್':'syllabus',
        'ದಾಖಲೆಗಳು':'documents'
    },
    'te': {
        'కాలేజీ': 'college',
        'హాస్టెల్': 'hostel',
        'శిక్షణ': 'education',
        'ఫీజు': 'fees',
        'సంప్రదించండి': 'contact',
        'ಟ್ರೈన్స్పొర్ట':'transport',
        'స్థాపకులు':'founder',
        'పరిశోధన':'research',
        'ర్యాగింగ్':'ragging',
        'క్రీడా':'sports',
        'సెలవు':'vacation',
        'స్కాలర్షిప్':'scholorship',
        'ప్రిన్సిపాల్':'principal',
        'లైబ్రరీ':'library',
        'సిలబస్':'syllabus'
    }
}

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word not in ignore_words and word.lower() not in stop_words]
    return ' '.join(tokens)

def translate_predefined_words(text, language):
    if language in predefined_words:
        words_dict = predefined_words[language]
        tokens = text.split()
        translated_tokens = [words_dict.get(token, token) for token in tokens]
        return ' '.join(translated_tokens)
    return text

# Build chatbot intent corpus
for intent in intents_data['intents']:
    for pattern in intent['patterns']:
        corpus.append(preprocess_text(pattern))
        tags.append(intent['tag'])

# Vectorize intent corpus
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Spell correction function
def correct_spelling(text):
    words = text.split()
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]
    return ' '.join(corrected_words)

# Chatbot response
def get_bot_response(user_input, language='en'):
    # Translate predefined words
    user_input = translate_predefined_words(user_input, language)

    # Preprocess input
    user_input_str = preprocess_text(user_input)
    user_input_vec = vectorizer.transform([user_input_str])

    # Calculate cosine similarity
    similarities = cosine_similarity(user_input_vec, X).flatten()
    max_similarity_index = np.argmax(similarities)

    if similarities[max_similarity_index] > 0.4:  # Threshold
        best_match_tag = tags[max_similarity_index]
        for intent in intents_data['intents']:
            if intent['tag'] == best_match_tag:
                response = random.choice(intent['responses'])
                break
    else:
        # Fallback to spelling correction
        corrected_input = correct_spelling(user_input)
        if corrected_input.lower() != user_input.lower():
            response = f"Did you mean: '{corrected_input}'? Sorry, I still don't understand."
        else:
            response = "I'm sorry, I don't understand. Please try rephrasing your question."

    # Translate response to selected language (if needed)
    if language != 'en':
        translator = Translator()
        response = translator.translate(response, src='en', dest=language).text

    return response

# Flask Routes
@app.route('/')
def index():
    session.clear()
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s AND password = %s", (user_id, password))
        user = cur.fetchone()
        cur.close()

        if user:
            flash('Logged in successfully!', 'success')
            return render_template('chat.html', user_id=user_id)
        else:
            flash('Invalid ID or Password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (id, password) VALUES (%s, %s)", (user_id, password))
            mysql.connection.commit()
            flash('You have successfully registered!', 'success')
            return render_template('chat.html', user_id=user_id)
        except IntegrityError:
            mysql.connection.rollback()
            flash('This ID is already taken. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        finally:
            cur.close()
    return render_template('register.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    This route handles chatbot queries.
    If the query is an FAQ, it should be handled on the front end.
    Only unmatched queries are sent here.
    """
    user_input = request.form['user_input']
    language = request.form['lang']  # Get the selected language from the request
    response = get_bot_response(user_input, language)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
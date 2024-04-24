from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import nltk

# Download NLTK resources if not already downloaded
nltk.download('wordnet')

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/checkPasswordComplexity', methods=['POST'])
def check_password_complexity():
    password = request.json.get('password')
    print("Received password:", password) # Log the received password

    # Check password complexity
    is_weak = not is_password_strong(password)
    alternative_password = None

    if is_weak:
        # Generate alternative strong password
        alternative_password = generate_strong_password()

    return jsonify({
        "is_weak": is_weak,
        "alternative_password": alternative_password
    })

def is_password_strong(password):
    # Password complexity logic
    return (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in '!@#$%^&*()-_=+{};:,<.>/?[]\\' for char in password) and
        not contains_common_word(password)
    )

def contains_common_word(password):
    # Check if the password contains common words/names using NLTK WordNet corpus
    common_words = set(nltk.corpus.words.words())
    password_lower = password.lower()  # Convert password to lowercase for case-insensitive comparison
    return any(word in password_lower for word in common_words)

def generate_strong_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()-_=+{};:,<.>/?[]\\'

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password with required components
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

if __name__ == '__main__':
    app.run(debug=False)

from app_init import request

from flask import render_template, session, redirect, url_for, make_response, jsonify
from functools import wraps
import requests
from app_init import app

def with_sidebar(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return render_template(f.__name__.replace('_route', '.html'), with_sidebar=True)
    return decorated_function

@app.route("/")
def landing_route():
    return render_template("landing.html", with_sidebar=False)

@app.route("/profile")
def profile_route():
    return render_template("profile.html", with_sidebar=True)

@app.route("/learn")
def learn_route():
    words = [
        # Animals
        {"kannada": "ಕರಡಿ", "english": "bear", "category": "Animals", "transliteration": "karadi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/bear.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/bear.wav"},
        {"kannada": "ಪಕ್ಷಿ", "english": "bird", "category": "Animals", "transliteration": "pakshi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/bird.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/bird.wav"},
        {"kannada": "ಚಿಟ್ಟೆ", "english": "butterfly", "category": "Animals", "transliteration": "chitte", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/butterfly.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/butterfly.wav"},
        {"kannada": "ಬೆಕ್ಕು", "english": "cat", "category": "Animals", "transliteration": "bekku", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/cat.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/cat.wav"},
        {"kannada": "ಕೋಳಿ", "english": "hen", "category": "Animals", "transliteration": "koli", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/hen.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/hen.wav"},
        {"kannada": "ಹಸು", "english": "cow", "category": "Animals", "transliteration": "hasu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/cow.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/cow.wav"},
        {"kannada": "ಮೊಸಳೆ", "english": "crocodile", "category": "Animals", "transliteration": "mosale", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/crocodile.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/crocodile.wav"},
        {"kannada": "ಜಿಂಕೆ", "english": "deer", "category": "Animals", "transliteration": "jinke", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/deer.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/deer.wav"},
        {"kannada": "ನಾಯಿ", "english": "dog", "category": "Animals", "transliteration": "naayi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/dog.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/dog.wav"},
        {"kannada": "ಬಾತುಕೋಳಿ", "english": "duck", "category": "Animals", "transliteration": "baatukoli", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/duck.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/duck.wav"},
        {"kannada": "ಆನೆ", "english": "elephant", "category": "Animals", "transliteration": "aane", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/elephant.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/elephant.wav"},
        {"kannada": "ನರಿ", "english": "fox", "category": "Animals", "transliteration": "nari", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/fox.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/fox.wav"},
        {"kannada": "ಕಪ್ಪೆ", "english": "frog", "category": "Animals", "transliteration": "kappe", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/frog.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/frog.wav"},
        {"kannada": "ಮೇಕೆ", "english": "goat", "category": "Animals", "transliteration": "meke", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/goat.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/goat.wav"},
        {"kannada": "ನೀರಾನೆ", "english": "hippopotamus", "category": "Animals", "transliteration": "neerane", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/hippopotamus.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/hippopotamus.wav"},
        {"kannada": "ಕುದುರೆ", "english": "horse", "category": "Animals", "transliteration": "kudure", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/horse.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/horse.wav"},
        {"kannada": "ಕತ್ತೆ", "english": "donkey", "category": "Animals", "transliteration": "katthe", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/donkey.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/donkey.wav"},
        {"kannada": "ಚಿರತೆ", "english": "leopard", "category": "Animals", "transliteration": "chirate", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/leopard.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/leopard.wav"},
        {"kannada": "ಸಿಂಹ", "english": "lion", "category": "Animals", "transliteration": "simha", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/lion.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/lion.wav"},
        {"kannada": "ಕೋತಿ", "english": "monkey", "category": "Animals", "transliteration": "kothi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/monkey.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/monkey.wav"},
        {"kannada": "ಹಂದಿ", "english": "pig", "category": "Animals", "transliteration": "handi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/pig.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/pig.wav"},
        {"kannada": "ನಾಯಿಮರಿ", "english": "puppy", "category": "Animals", "transliteration": "naayimari", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/puppy.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/puppy.wav"},
        {"kannada": "ಮೊಲ", "english": "rabbit", "category": "Animals", "transliteration": "mola", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/rabbit.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/rabbit.wav"},
        {"kannada": "ಘೇಂಡಾಮೃಗ", "english": "rhino", "category": "Animals", "transliteration": "gendamruga", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/rhino.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/rhino.wav"},
        {"kannada": "ಹುಂಜ", "english": "rooster", "category": "Animals", "transliteration": "hunja", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/rooster.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/rooster.wav"},
        {"kannada": "ತಿಮಿಂಗಿಲ", "english": "shark", "category": "Animals", "transliteration": "timingila", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/shark.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/shark.wav"},
        {"kannada": "ಕುರಿ", "english": "sheep", "category": "Animals", "transliteration": "kuri", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/sheep.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/sheep.wav"},
        {"kannada": "ಹುಲಿ", "english": "tiger", "category": "Animals", "transliteration": "huli", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/tiger.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/tiger.wav"},
        {"kannada": "ಆಮೆ", "english": "tortoise", "category": "Animals", "transliteration": "aame", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/tortoise.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/tortoise.wav"},
        {"kannada": "ಕಾಗೆ", "english": "crow", "category": "Animals", "transliteration": "kaage", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/crow.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/crow.wav"},
        {"kannada": "ನವಿಲು", "english": "peacock", "category": "Animals", "transliteration": "navilu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/peacock.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/peacock.wav"},
        
        # Items
        {"kannada": "ವಿಮಾನ", "english": "aeroplane", "category": "Items", "transliteration": "vimaana", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/aeroplane.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/aeroplane.wav"},
        {"kannada": "ಹಡಗು", "english": "ship", "category": "Items", "transliteration": "hadagu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/ship.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/ship.wav"},
        {"kannada": "ದೋಣಿ", "english": "boat", "category": "Items", "transliteration": "doni", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/boat.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/boat.wav"},
        {"kannada": "ಚೆಂಡು", "english": "ball", "category": "Items", "transliteration": "chendu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/ball.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/ball.wav"},
        {"kannada": "ಕನ್ನಡಕ", "english": "spectacles", "category": "Items", "transliteration": "kannadaka", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/spectacles.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/spectacles.wav"},
        {"kannada": "ಮೇಣದಬತ್ತಿ", "english": "candle", "category": "Items", "transliteration": "menadabatti", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/candle.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/candle.wav"},
        {"kannada": "ಬಟ್ಟೆ", "english": "clothes", "category": "Items", "transliteration": "batte", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/clothes.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/clothes.wav"},
        {"kannada": "ಹೂವು", "english": "flower", "category": "Items", "transliteration": "huuvu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/flower.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/flower.wav"},
        {"kannada": "ಚಮಚ", "english": "spoon", "category": "Items", "transliteration": "chamacha", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/spoon.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/spoon.wav"},
        {"kannada": "ಬೀಗ", "english": "lock", "category": "Items", "transliteration": "beega", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/lock.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/lock.wav"},
        {"kannada": "ಕತ್ತರಿ", "english": "scissor", "category": "Items", "transliteration": "kattari", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/scissor.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/scissor.wav"},
        {"kannada": "ಕಪ್ಪೆಚಿಪ್ಪು", "english": "seashell", "category": "Items", "transliteration": "kappechippu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/seashell.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/seashell.wav"},
        {"kannada": "ಮರ", "english": "tree", "category": "Items", "transliteration": "mara", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/tree.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/tree.wav"},
        {"kannada": "ಮನೆ", "english": "house", "category": "Items", "transliteration": "mane", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/house.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/house.wav"},
        {"kannada": "ಕಿಟಕಿ", "english": "window", "category": "Items", "transliteration": "kitaki", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/window.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/window.wav"},
        {"kannada": "ಬಾಗಿಲು", "english": "door", "category": "Items", "transliteration": "baagilu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/door.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/door.wav"},
        {"kannada": "ಪುಸ್ತಕ", "english": "book", "category": "Items", "transliteration": "pustaka", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/book.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/book.wav"},
        {"kannada": "ಕುರ್ಚಿ", "english": "chair", "category": "Items", "transliteration": "kurchi", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/chair.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/chair.wav"},
        {"kannada": "ಮೇಜು", "english": "table", "category": "Items", "transliteration": "meju", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/table.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/table.wav"},
        {"kannada": "ಗಡಿಯಾರ", "english": "clock", "category": "Items", "transliteration": "gadiyaara", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/clock.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/clock.wav"},
        {"kannada": "ಲೋಟ", "english": "cup", "category": "Items", "transliteration": "lota", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/cup.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/cup.wav"},
        {"kannada": "ತಟ್ಟೆ", "english": "plate", "category": "Items", "transliteration": "tatte", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/plate.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/plate.wav"},
        {"kannada": "ಚೊಂಬು", "english": "jug", "category": "Items", "transliteration": "chombu", "image_url": "https://upcdn.io/kW15bgo/raw/learnkannada/images/jug.png", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/jug.wav"}
    ]
    return render_template("learn.html", words=words, with_sidebar=True)


@app.route("/check_audio", methods=['POST'])
def check_audio():
    audio_url = request.json.get('audio_url')
    try:
        response = requests.head(audio_url, timeout=5)
        return jsonify({"status": response.status_code == 200})
    except requests.RequestException:
        return jsonify({"status": False})

@app.route("/logout", methods=['POST'])
def logout_route():
    session.clear()
    return redirect(url_for('landing_route'))

@app.route("/quiz", methods=['GET', 'POST'])
def quiz_route():
    words = [
        # Animals
        {"kannada": "ಕರಡಿ", "english": "bear", "category": "Animals", "transliteration": "karadi", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/bear.wav"},
        {"kannada": "ಪಕ್ಷಿ", "english": "bird", "category": "Animals", "transliteration": "pakshi", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/bird.wav"},
        {"kannada": "ಚಿಟ್ಟೆ", "english": "butterfly", "category": "Animals", "transliteration": "chitte", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/butterfly.wav"},
        {"kannada": "ಬೆಕ್ಕು", "english": "cat", "category": "Animals", "transliteration": "bekku", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/cat.wav"},
        {"kannada": "ಕೋಳಿ", "english": "hen", "category": "Animals", "transliteration": "koli", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/hen.wav"},
        {"kannada": "ಹಸು", "english": "cow", "category": "Animals", "transliteration": "hasu", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/cow.wav"},
        {"kannada": "ಮೊಸಳೆ", "english": "crocodile", "category": "Animals", "transliteration": "mosale", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/crocodile.wav"},
        {"kannada": "ಜಿಂಕೆ", "english": "deer", "category": "Animals", "transliteration": "jinke", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/deer.wav"},
        {"kannada": "ನಾಯಿ", "english": "dog", "category": "Animals", "transliteration": "naayi", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/dog.wav"},
        {"kannada": "ಬಾತುಕೋಳಿ", "english": "duck", "category": "Animals", "transliteration": "baatukoli", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/duck.wav"},
        {"kannada": "ಆನೆ", "english": "elephant", "category": "Animals", "transliteration": "aane", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/elephant.wav"},
        {"kannada": "ನರಿ", "english": "fox", "category": "Animals", "transliteration": "nari", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/fox.wav"},
        {"kannada": "ಕಪ್ಪೆ", "english": "frog", "category": "Animals", "transliteration": "kappe", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/frog.wav"},
        {"kannada": "ಮೇಕೆ", "english": "goat", "category": "Animals", "transliteration": "meke", "audio_url": "https://upcdn.io/kW15bgo/raw/learnkannada/audio/goat.wav"}
    ]

    import random

    if request.method == 'GET':
        # Generate quiz questions
        quiz_words = random.sample(words, 10)
        quiz_questions = []

        for word in quiz_words:
            # Randomly choose question type
            question_type = random.choice(['kannada_to_english', 'english_to_kannada', 'audio_listening'])

            if question_type == 'kannada_to_english':
                # Create a question asking to translate Kannada to English
                incorrect_options = random.sample([w for w in words if w != word], 3)
                options = [word['english']] + [w['english'] for w in incorrect_options]
                random.shuffle(options)

                quiz_questions.append({
                    'type': 'kannada_to_english',
                    'question': f"What is the English translation of '{word['kannada']}'?",
                    'correct_answer': word['english'],
                    'options': options,
                    'kannada_word': word['kannada']
                })
            elif question_type == 'english_to_kannada':
                # Create a question asking to match English to Kannada
                incorrect_options = random.sample([w for w in words if w != word], 3)
                options = [word['kannada']] + [w['kannada'] for w in incorrect_options]
                random.shuffle(options)

                quiz_questions.append({
                    'type': 'english_to_kannada',
                    'question': f"What is the Kannada script for '{word['english']}'?",
                    'correct_answer': word['kannada'],
                    'options': options,
                    'english_word': word['english']
                })
            else:
                # Create an audio listening question
                incorrect_options = random.sample([w for w in words if w != word], 3)
                options = [word['english']] + [w['english'] for w in incorrect_options]
                random.shuffle(options)

                quiz_questions.append({
                    'type': 'audio_listening',
                    'question': "Listen to the audio and identify the word",
                    'correct_answer': word['english'],
                    'options': options,
                    'audio_url': word['audio_url']
                })

        # Store quiz data in session
        session['quiz_questions'] = quiz_questions
        session['quiz_score'] = 0
        session['current_question_index'] = 0
        session['incorrect_answers'] = []

        return render_template('quiz.html', 
                               question=quiz_questions[0], 
                               question_number=1, 
                               total_questions=len(quiz_questions))

    elif request.method == 'POST':
        # Process quiz answer
        quiz_questions = session.get('quiz_questions', [])
        current_index = session.get('current_question_index', 0)
        user_answer = request.form.get('answer')

        # Check if answer is correct
        current_question = quiz_questions[current_index]
        is_correct = user_answer == current_question['correct_answer']

        if is_correct:
            session['quiz_score'] += 1
        else:
            # Track incorrect answers
            incorrect_answer = {
                'question': current_question['question'],
                'user_answer': user_answer,
                'correct_answer': current_question['correct_answer']
            }
            session['incorrect_answers'].append(incorrect_answer)

        # Move to next question or end quiz
        current_index += 1
        session['current_question_index'] = current_index

        if current_index < len(quiz_questions):
            return render_template('quiz.html', 
                                   question=quiz_questions[current_index], 
                                   question_number=current_index + 1, 
                                   total_questions=len(quiz_questions), 
                                   previous_correct=is_correct,
                                   correct_answer=current_question['correct_answer'])
        else:
            # Quiz completed
            final_score = session.get('quiz_score', 0)
            total_questions = len(quiz_questions)
            percentage = (final_score / total_questions) * 100
            incorrect_answers = session.get('incorrect_answers', [])

            return render_template('quiz_result.html', 
                                   score=final_score, 
                                   total_questions=total_questions, 
                                   percentage=percentage,
                                   incorrect_answers=incorrect_answers)
            return render_template('quiz_result.html', 
                                   score=final_score, 
                                   total_questions=total_questions, 
                                   percentage=percentage)
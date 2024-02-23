from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=app.questions)

@app.route('/questions')
def get_questions():
    return jsonify(app.questions)

if __name__ == "__main__":
    app.questions = [
        {
            "question": "Where is Mt. Everest Located?",
            "options": ["a. Nepal", "b. India", "c. Sri Lanka", "d. Japan"],
            "correct_answer": "a"
        },
        {
            "question": "Which team is the winner of IPL 2021?",
            "options": ["a. MI", "b. RCB", "c. CSK", "d. KKR"],
            "correct_answer": "c"
        },
        {
            "question": "Who is the father of Computer?",
            "options": ["a. Albert Einstein", "b. Phunsukh Wangdu", "c. Elon Musk", "d. Charles Babbage"],
            "correct_answer": "d"
        }
    ]
    app.run(host='0.0.0.0', port=5000, debug=True)

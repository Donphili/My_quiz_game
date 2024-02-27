const quizForm = document.getElementById('quiz-form');
const questionContainer = document.getElementById('question');
const optionsContainer = document.getElementById('options');
const resultContainer = document.getElementById('result');

let currentQuestion = 0;
let score = 0;

function displayQuestion() {
    const question = questions[currentQuestion];
    questionContainer.textContent = question.prompt;
    optionsContainer.innerHTML = '';
    question.options.forEach(option => {
        const button = document.createElement('button');
        button.textContent = option.text;
        button.addEventListener('click', () => checkAnswer(option.correct));
        optionsContainer.appendChild(button);
    });
}

function checkAnswer(correct) {
    if (correct) {
        score++;
    }
    currentQuestion++;
    if (currentQuestion < questions.length) {
        displayQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    quizForm.style.display = 'none';
    resultContainer.textContent = `You scored ${score} out of ${questions.length}.`;
}

quizForm.addEventListener('submit', (e) => {
    e.preventDefault();
});

displayQuestion();

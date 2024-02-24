document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('options-form');
    const submitButton = document.getElementById('submit-btn');
    const questionContainer = document.getElementById('question-container');                                                             
    const questions = [
        {
            "question": "Where is Mt. Everest Located?",
            "options": ["a. Nepal", "b. India", "c. Sri Lanka", "d. Japan"],
            "correct_answer": 0
        },
        {
            "question": "Which team is the winner of IPL 2021?",
            "options": ["a. MI", "b. RCB", "c. CSK", "d. KKR"],
            "correct_answer": 2
        },
        {
            "question": "Who is the father of Computer?",
            "options": ["a. Albert Einstein", "b. Phunsukh Wangdu", "c. Elon Musk", "d. Charles Babbage"],
            "correct_answer": 3
        }
    ];
    let currentQuestionIndex = 0;                                  
    
    // Function to display current question
    function displayQuestion() {
        const question = questions[currentQuestionIndex];
        const optionsForm = `
            <form id="options-form">
                <p>${question.question}</p>
                ${question.options.map((option, index) => `
                    <label><input type="radio" name="option" value="${index}"> ${option}</label><br>
                `).join('')}
            </form>
        `;
        questionContainer.innerHTML = optionsForm;
    }

    // Function to handle form submission
    function handleSubmit(event) {
        event.preventDefault();

        // Get selected option
        const selectedOption = form.querySelector('input[name="option"]:checked');
        if (!selectedOption) {
            alert('Please select an option.');
            return;
        }

        // Get question
        const question = questions[currentQuestionIndex];

        // Get correct answer
        const correctAnswerIndex = question.correct_answer;
        const correctAnswer = question.options[correctAnswerIndex];

        // Check if selected answer is correct
        if (selectedOption.value === correctAnswerIndex.toString()) {
            alert('Correct!');
        } else {
            alert('Incorrect! The correct answer is: ' + correctAnswer);
        }

        // Move to next question or end if all questions are done
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion();
        } else {
            alert('Quiz completed! No more questions.');
            questionContainer.innerHTML = ''; // Clear question container
        }
    }

    // Add event listener for form submission
    submitButton.addEventListener('click', handleSubmit);

    // Display first question when page loads
    displayQuestion();
});

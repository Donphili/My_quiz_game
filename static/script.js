document.addEventListener("DOMContentLoaded", function() {
    const questionElement = document.getElementById("question");
    const optionsElements = [document.getElementById("option0"), document.getElementById("option1"), document.getElementById("option2"), document.getElementById("option3")];
    const formElement = document.getElementById("options-form");
    const submitButton = document.getElementById("submit-btn");

    let currentQuestion = 0;
    let totalQuestions = 0;

    function loadQuestion(questionData) {
        questionElement.textContent = questionData.question;
        questionData.options.forEach((option, index) => {
            optionsElements[index].textContent = option;
        });
    }

    function checkAnswer() {
        const selectedOption = formElement.querySelector('input[name="option"]:checked');
        if (!selectedOption) {
            alert("Please select an option.");
            return;
        }
        const selectedValue = selectedOption.value;
        const correctAnswer = questions[currentQuestion].correct_answer;
        if (selectedValue === correctAnswer) {
            alert("Your answer is correct!");
        } else {
            alert("Your answer is incorrect!");
        }
        currentQuestion++;
        if (currentQuestion < totalQuestions) {
            loadQuestion(questions[currentQuestion]);
        } else {
            alert("Quiz Finished! You have completed the quiz.");
            // Redirect or perform any other action here after finishing the quiz
        }
    }

    loadQuestion(questions[currentQuestion]);
    totalQuestions = questions.length;

    submitButton.addEventListener("click", checkAnswer);
});

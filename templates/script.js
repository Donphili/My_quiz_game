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
        questionContainer.innerHTML = 'Correct!';
    } else {
        questionContainer.innerHTML = 'Incorrect! The correct answer is: ' + correctAnswer;
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

#!/usr/bin/env python

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    """
    Checks if the user's answer matches the correct answer.
    Returns True if correct, False otherwise.
    """
    return user_answer.lower() == correct_answer.lower()

# Function to handle scoring
def calculate_score(questions, user_answers):
    """
    Calculates the user's score based on their answers.
    Returns the score as a percentage.
    """
    num_correct = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        if check_answer(user_answers[i], question['correct_answer']):
            num_correct += 1

    return (num_correct / total_questions) * 100

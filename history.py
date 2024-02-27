#!/usr/bin/env python

# Function to display the quiz history
def display_history(history):
    """
    Displays the quiz history in a formatted way.
    """
    # Checks if the history is empty
    if not history:
        return "Quiz history is empty."

    # Builds the formatted history string
    result = "Quiz History:\n"
    for i, quiz in enumerate(history, start=1):
        result += f"{i}. Question: {quiz['question']}\n"
        result += f"   Answer: {quiz['user_answer']}\n"
        result += f"   Correct Answer: {quiz['correct_answer']}\n\n"

    return result

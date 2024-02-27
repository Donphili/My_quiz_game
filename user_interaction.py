# Function to handle user interaction
def handle_user_interaction(questions):
    """
    Displays questions to the user and checks their answers.
    """
    for question in questions:
        print(question['question'])
        for idx, option in enumerate(question['options']):
            print(f"{chr(97 + idx)}. {option}")
        
        user_answer = input("Your answer: ").lower()
        correct_answer = chr(97 + question['correct_answer'])
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

# This script assumes that 'questions' is defined elsewhere.
# Make sure this variable is available or modify the script accordingly.

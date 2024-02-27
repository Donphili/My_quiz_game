from questions import questions

def run_quiz():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", score, "out of", len(questions), "questions correct.")

if __name__ == "__main__":
    run_quiz()

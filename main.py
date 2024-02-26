import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.current_question = 0
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest mammal?", "answer": "Blue whale"}
        ]
        
        self.label = tk.Label(master, text="")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        self.next_button = tk.Button(master, text="Next Question", command=self.next_question)
        self.next_button.pack()

        self.display_question()

    def display_question(self):
        self.label.config(text=self.questions[self.current_question]["question"])
        self.entry.delete(0, tk.END)

    def check_answer(self):
        answer = self.entry.get()
        correct_answer = self.questions[self.current_question]["answer"]
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "You got it right!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")

    def next_question(self):
        self.current_question = (self.current_question + 1) % len(self.questions)
        self.display_question()

root = tk.Tk()
app = QuizGame(root)
root.mainloop()

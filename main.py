import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        
        self.current_question = 0
        self.questions = [
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
        
        self.create_widgets()
        
    def create_widgets(self):
        self.question_label = tk.Label(self, text="")
        self.question_label.pack(pady=10)
        
        self.option_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self, text="", variable=self.option_var, value=str(i))
            btn.pack(anchor="w")
            self.option_buttons.append(btn)
            
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.load_question(0)
        
    def load_question(self, question_idx):
        question_data = self.questions[question_idx]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

        self.option_var.set(None)
        
    def check_answer(self):
        selected_option = self.option_var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_option == correct_answer:
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect!")
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question(self.current_question)
        else:
            messagebox.showinfo("Quiz Finished", "You have completed the quiz!")
            self.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()

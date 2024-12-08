import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, username, password):
        return self.username == username and self.password == password

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, selected_option):
        return selected_option == self.correct_answer

class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def submit_answer(self, selected_option):
        question = self.get_current_question()
        if question.check_answer(selected_option):
            self.score += 1
        self.current_question_index += 1

    def has_next_question(self):
        return self.current_question_index < len(self.questions)

class QuizApp:
    def __init__(self, root, user, quiz):
        self.root = root
        self.user = user
        self.quiz = quiz
        self.root.title("Online Quiz System")
        self.root.geometry("400x300")  # Set window size to 400x300 pixels
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        self.label_username = tk.Label(self.root, text="Username")
        self.label_username.pack(pady=(50, 5))  # Add top padding

        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Password")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack(pady=20)  # Add top padding

    def create_quiz_screen(self):
        self.clear_screen()
        self.display_question()

    def display_question(self):
        if self.quiz.has_next_question():
            question = self.quiz.get_current_question()
            self.label_question = tk.Label(self.root, text=question.text, wraplength=300)
            self.label_question.pack(pady=(50, 20))  # Add top padding

            self.var_option = tk.StringVar()

            for option in question.options:
                radio = tk.Radiobutton(self.root, text=option, variable=self.var_option, value=option)
                radio.pack(anchor='w', padx=20)  # Add left padding and align left

            self.button_next = tk.Button(self.root, text="Next", command=self.next_question)
            self.button_next.pack(pady=20)  # Add top padding
        else:
            self.display_result()

    def next_question(self):
        selected_option = self.var_option.get()
        self.quiz.submit_answer(selected_option)
        self.clear_screen()
        self.display_question()

    def display_result(self):
        self.clear_screen()
        result_text = f"Quiz Completed! Your score is: {self.quiz.score}/{len(self.quiz.questions)}"
        self.label_result = tk.Label(self.root, text=result_text)
        self.label_result.pack(pady=(100, 0))  # Add top padding

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.user.check_credentials(username, password):
            self.create_quiz_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()

    # Sample user
    user = User("admin", "admin")

    # Sample questions
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        Question("What is the color of the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue")
    ]

    # Sample quiz
    quiz = Quiz("Sample Quiz", questions)

    # Start the application
    app = QuizApp(root, user, quiz)
    root.mainloop()

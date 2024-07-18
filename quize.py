import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import json
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("300x200")

        self.background_image = ImageTk.PhotoImage(Image.open("C:/Users/LENOVO/Documents/vs code/python/projects/quize/background.jpg"))

        self.root.configure(bg="lightgray")
        self.root.background = self.background_image
        self.root.bg_label = tk.Label(root, image=self.background_image)
        self.root.bg_label.place(relwidth=1, relheight=1)

        self.label_name = tk.Label(root, text="Enter your name:", font=("Arial", 12))
        self.entry_name = tk.Entry(root, font=("Arial", 12))
        self.label_id = tk.Label(root, text="Enter your ID:", font=("Arial", 12))
        self.entry_id = tk.Entry(root, font=("Arial", 12))
        self.start_button = tk.Button(root, text="Start Quiz", command=self.open_quiz_window, font=("Arial", 12), bg="green", fg="white")

        self.label_name.pack(pady=10)
        self.entry_name.pack()
        self.label_id.pack(pady=10)
        self.entry_id.pack()
        self.start_button.pack(pady=10)

    def open_quiz_window(self):
       self.root.withdraw()
       
       self.quiz_window = tk.Toplevel(self.root)
       self.quiz_window.title("Python Quiz: Choose Options Carefully")
       self.quiz_window.geometry("800x300")

   


       with open("C:/Users/LENOVO/Documents/vs code/python/projects/quize/questions.txt", "r") as text_file:
           self.questions = json.load(text_file)

       self.score = 0
       self.current_question = 0
       self.var_answer = tk.StringVar()

       self.show_next_question()

    def show_next_question(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()

        question_data = self.questions[self.current_question]
        question_label = tk.Label(self.quiz_window, text=question_data["question"], font=("Arial", 12))
        question_label.pack(pady=10)

        for i, option in enumerate(question_data["options"]):
            rb = tk.Radiobutton(self.quiz_window, text=option, value=option, variable=self.var_answer)
            rb.pack(anchor="w")

        next_button = tk.Button(self.quiz_window, text="Next", command=self.next_question, font=("Arial", 12), bg="blue", fg="white")
        next_button.pack(pady=10)


    def next_question(self):
        user_answer = self.var_answer.get()
        correct_answer = self.questions[self.current_question]["answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_next_question()
        else:
            self.show_results()

    def show_results(self):
        messagebox.showinfo("Results", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.score_label = Label(text=f"Score: 0", fg="#FFFFFF", bg=THEME_COLOR, font=("Arial", 16, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="smth", width=280, font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_img = PhotoImage(file="images/true.png")
        self.correct = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.correct.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.incorrect = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.incorrect.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the quiz")
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")


    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)


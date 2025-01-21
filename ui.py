from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=30, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="This is the text",
            fill=THEME_COLOR,
            font=("Liberation Sans", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.say_false)
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.say_true)
        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def say_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def say_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



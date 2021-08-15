from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND_COLOR = "#375362"


class QuizUI:
    def __init__(self, quizbrain):
        self.quizbrain = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Questions', fill='black',
                                                     font=("Ariel", 20, "italic"), width=200)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=BACKGROUND_COLOR)
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="false.png")
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quizbrain.is_question_available():
            self.score_label.config(text=f'Score: {self.quizbrain.score}')
            q = self.quizbrain.next_question()
            self.canvas.itemconfig(self.question_text, text=q)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        feedback = self.quizbrain.check_answer("True")
        self.give_feedback(feedback)

    def false_pressed(self):
        feedback = self.quizbrain.check_answer("False")
        self.give_feedback(feedback)

    def give_feedback(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)

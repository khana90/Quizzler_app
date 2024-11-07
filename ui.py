from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_lbl= Label(text="Score:0", fg= "white", bg=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1)

        self.canvas=Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(
            150, 125, width= 280, text="some txt", fill=THEME_COLOR,font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.tru_btn=Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.tru_btn.grid(row=2, column=0)

        fals_img= PhotoImage(file="images/false.png")
        self.fals_btn=Button(image=fals_img, highlightthickness=0, command=self.false_pressed)
        self.fals_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if  self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_lbl.config(text= f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=" you have reached the end of quiz")

    def true_pressed(self):
        is_right= self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
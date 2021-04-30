from tkinter import *
import html
import requests

THEME_COLOR = "#375362"

class Question:
    def __init__(self):
        self.ques_no = 0
        self.score = 0
        self.ques = []
        self.cur_ques = dict()
        self.get_ques()
        self.ui()
    
    def get_ques(self):
        parameter = {'amount' :10,'type':'boolean'}

        try:
            response = requests.get(url='http://opentdb.com/api.php',params=parameter)
            data= response.json()
            self.ques= data['results']

        except Exception as e:
            print(e)
    
    def ui(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",fg='white',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=350,height=250,bg='white')
        self.ques_text = self.canvas.create_text(150,125,text=self.next_ques(),fill=THEME_COLOR,font=("Arial",14))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file="Modules_Python/Request_api/quiz app/true.png")
        self.true_btn = Button(image=true_image,highlightthickness=0,height=160,width=160,command=self.true_ans)
        self.true_btn.grid(row=2,column=0)

        self.false_btn = Button(text='False',highlightthickness=0,height=3,width=7,font=('Arial',30),command=self.false_ans)
        self.false_btn.grid(row=2,column=1)

        self.window.mainloop()
    
    def next_ui_ques(self):
        self.canvas.itemconfig(self.ques_text,text=self.next_ques())

    def next_ques(self):
        self.cur_ques = self.ques[self.ques_no]
        self.ques_no = self.ques_no + 1
        return html.unescape(self.cur_ques['question'])

    def true_ans(self):
        if self.ques_no <len(self.ques):
            ans = 'True'
            if ans == self.cur_ques['correct_answer']:
                print('Correct')
                self.score = self.score+1
            else:
                print(f"Correct answer is : {self.cur_ques['correct_answer']}")
            self.is_ques_remaining()
        
    def false_ans(self):
        if self.ques_no <len(self.ques):
            ans = 'False'
            if ans == self.cur_ques['correct_answer']:
                print('Correct')
                self.score = self.score+1
            else:
                print(f"Correct answer is : {self.cur_ques['correct_answer']}")
            self.is_ques_remaining()

    def is_ques_remaining(self):
        self.score_label.config(text=f"Score: {self.score}")
        if self.ques_no <len(self.ques):
            self.next_ui_ques()
        else:
            print(f"Your score is : {self.score}")


ques1 = Question()
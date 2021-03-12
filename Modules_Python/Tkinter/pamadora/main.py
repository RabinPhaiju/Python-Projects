from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#69F129"
YELLOW = "#f7f5dd"
WHITE = '#ffffff'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = '✔'
resps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start.config(command='',text='Work')
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60
    if resps in [0,2,4,6]:
        timer_label.config(text= 'Work',fg=GREEN)
        count_down(work_sec)
    elif resps in [1,3,5]:
        timer_label.config(text= 'Break',fg=RED)
        count_down(short_break_sec)
    elif resps == 7:
        count_down(long_break_min)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global resps
    min = count//60
    sec = count-min*60
    if sec<10:
        sec = f'0{sec}'
    if min<10:
        min = f'0{min}'
    time = f'{min}:{sec}'
    canvas.itemconfig(timer_text,text=time)
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    elif count==0 and resps==7:
        reset_clicked()
        timer_tick.config(text='')
    else:
        resps += 1
        global tick
        ticks = tick*resps
        timer_tick.config(text=ticks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(height=400,width=400)
window.maxsize(height=400,width=400)
window.config(padx=20,pady=20,bg=WHITE)
window.title('Work Timer')

timer_label = Label(text='Timer',font=(FONT_NAME,24,'bold'),fg=GREEN,bg=WHITE)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=280,height=280,bg=WHITE,highlightthickness=0)
work_img = PhotoImage(file="Modules_Python/Tkinter/pamadora/work.png")
break_img = PhotoImage(file="Modules_Python/Tkinter/pamadora/break.png")
canvas.create_image(140,142,image=work_img)
canvas.grid(row=1,column=1)

timer_text = canvas.create_text(140,100,text='00:00',fill='white',font=(FONT_NAME,22,'bold'))

start = Button(text='Start',command=start_timer,highlightthickness=0)
start.grid(row=2,column=0)

timer_tick = Label(text='',font=('Arial',20,'bold'),fg=GREEN,bg=WHITE)
timer_tick.grid(column=1,row=3)

def reset_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text= 'Timer',fg=GREEN)
    global resps
    resps= 0
    start.config(command=start_timer,text='Start')

    

reset = Button(text='Reset',command=reset_clicked,highlightthickness=0)
reset.grid(row=2,column=2)


window.mainloop()
from tkinter import *

window = Tk()
window.minsize(height=120,width=240)
window.maxsize(height=120,width=240)
window.title('Mies to Km')

# Label

my_label1 = Label(text='')
my_label1.grid(column=0,row=0)

my_label = Label(text='is equla to')
my_label.grid(column=1,row=2)
my_label3 = Label(text='0',font=('Arial',20))
my_label3.grid(column=2,row=2)
my_label4= Label(text='Km')
my_label4.grid(column=3,row=2)

#input
input_text = Entry(width=16)
input_text.grid(column=2,row=1)
my_label2 = Label(text='Miles')
my_label2.grid(column=3,row=1)


# button
def button_clicked():
    my_label3.config(text=int(input_text.get())*1.609)

fred = Button(text='Calculate',command=button_clicked)
fred.grid(column=2,row=3)


window.mainloop()
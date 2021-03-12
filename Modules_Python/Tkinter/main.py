from tkinter import *

window = Tk()
window.minsize(height=400,width=300)
window.maxsize(height=800,width=600)
window.title('Converter')

# Label
my_label = Label(text='New label',font=('Arial',24,'bold'))
my_label.grid(column=0,row=0)

# update label
# my_label.config(text='update')

#input
input_text = Entry(width=16)
input_text.grid(column=0,row=1)


# button
def button_clicked():
    my_label.config(text=input_text.get())

fred = Button(text='Submit',command=button_clicked)
# display in screen
#1 fred.pack()
#2 fred.place(x=180,y=36)
fred.grid(column=2,row=1)

# Text
text = Text(height=5,width=30)
text.focus()
text.insert(END,'This is a multiline text entry')
print(text.get('1.0',END))
text.grid(row=2,column=0)

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.grid(row=3,column=0)

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0,to=100,command=scale_used)
scale.grid(row=2,column=2)

# Checkbox
def checkbutton_used():
    print(check_state.get())

check_state = IntVar()
checkbutton = Checkbutton(text='is On?',variable=check_state,command=checkbutton_used)
checkbutton.grid(row=3,column=1)

# Radio button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
Radiobutton1 = Radiobutton(text='Option1',value=1,variable=radio_state,command=radio_used)
Radiobutton2 = Radiobutton(text='Option2',value=2,variable=radio_state,command=radio_used)
Radiobutton1.grid(row=4,column=0)
Radiobutton2.grid(row=4,column=1)

#List Box
def list_box(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['apple','pear','orange','papaya','grapes']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",list_box)
listbox.grid(row=5,column=0)


window.mainloop()
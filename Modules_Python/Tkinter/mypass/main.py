from tkinter import *
from tkinter import messagebox
import csv
import random
import clipboard
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [chr(x) for x in range(97,123)] + [chr(x) for x in range(65,91)]
numbers = [ x for x in range(0,10)]
symbols = [chr(x) for x in range(33,48) if chr(x) not in ['"',"'",',','.']]

def gen_pws():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password = [random.choice(letters) for _ in range(nr_letters)] + [random.choice(numbers) for _ in range(nr_numbers)]  + [random.choice(symbols) for _ in range(nr_symbols)]
    random.shuffle(password)
    psw = ''.join(map(str, password)) 
    clipboard.copy(psw)
    return psw

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    global website_input
    global email_iput
    global password_input
    website = website_input.get()
    email = email_iput.get()
    password = password_input.get()

    if len(website)<1 or len(email)<1 or len(password)<1:
        messagebox.showwarning(title='Details cannot be saved',message='Fields cannot be empty')
    else:
        user = [website,email,password]
        save_input = messagebox.askyesno(title='Do you want to save it',message=f'These are the details:\n{website}\n{email}\n{password}\n')
        if save_input:
            website_input.delete(0,END)
            email_iput.delete(0,END)
            password_input.delete(0,END)
            with open('Modules_Python/Tkinter/mypass/user.csv', 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(user)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(height=450,width=420)
window.maxsize(height=450,width=420)
window.config(padx=20,pady=10)
window.title('Password Manager')


canvas = Canvas(width=280,height=280,bg='#ffffff',highlightthickness=0)
my_pass_img = PhotoImage(file="Modules_Python/Tkinter/mypass/logo.png")

canvas.create_image(140,142,image=my_pass_img)
canvas.grid(row=0,column=0,columnspan=3)

# website : input type
website_text = Label(text='Website: ',font=('Arial',14))
website_text.grid(column=0,row=1)

website_input = Entry(width=40)
website_input.focus()
website_input.grid(column=1,row=1,columnspan=2)

# email : input type
email_text = Label(text='Email: ',font=('Arial',14))
email_text.grid(column=0,row=2)

email_iput = Entry(width=40)
email_iput.grid(column=1,row=2,columnspan=2)

# password : input type
password_text = Label(text='Password: ',font=('Arial',14))
password_text.grid(column=0,row=3)

password_input = Entry(width=22)
password_input.grid(column=1,row=3)

def button_clicked():
    password_input.delete(0,END)
    password_input.insert(0,gen_pws())

generate_password = Button(text='Generate Password',command=button_clicked)
generate_password.grid(column=2,row=3,columnspan=2)

add_button = Button(text='Add',command=add_button_clicked,width=40)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
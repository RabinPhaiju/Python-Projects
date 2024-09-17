import datetime
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

my_email = 'rabinphaiju@gmail.com'
password = 'enter your password'
html = Path('index.html').read_text()

with open('Learn_Python/SMTP/birthday_wish/birthdays.csv') as f:
    user_data = csv.reader(f)

    users =[x for x in user_data]
today_date = datetime.date.today()

email = EmailMessage()
email['from'] = 'rabin'

for user in users:
    if today_date.day == int(user[4]) and today_date.month == int(user[3]):
        with open('Learn_Python/SMTP/birthday_wish/letter.txt','r') as letter:
            letter_text = ''.join(map(str,letter.readlines())).replace('NAME',user[0])

            email['to'] = user[1]
            email['subject'] = 'Happy Birthday'
            email.set_content(
                html.substitute({'title':'Happy Birthday','name':user[0]})+letter_text,
                subtype='html'
            )

        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(email)

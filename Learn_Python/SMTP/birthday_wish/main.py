import datetime
import csv
import smtplib

my_email = 'rabinphaiju@gmail.com'
password = 'kdslfkjdslf'

with open('Learn_Python/SMTP/birthday_wish/birthdays.csv') as f:
    user_data = csv.reader(f)

    users =[x for x in user_data]
today_date = datetime.date.today()

for user in users:
    if today_date.day == int(user[4]) and today_date.month == int(user[3]):
        with open('Learn_Python/SMTP/birthday_wish/letter.txt','r') as letter:
            letter_text = ''.join(map(str,letter.readlines())).replace('NAME',user[0])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=user[1],
            msg=f'Subject:Happy Birthday\n\n {letter_text}'
            )

with open('./Learn_Python/File/mail_merger/invited_names.txt',"r") as names:
    invited_names  = (names.read())

names  = invited_names.split(',')
print(names)

with open('./Learn_Python/File/mail_merger/letter.txt',"r") as letter_format:
    format  = (letter_format.read())


for name in names:
    letter = format.replace('user',name)
    with open(f'./Learn_Python/File/mail_merger/output/letter_for_{name}.txt',"w") as new_letter:
        new_letter.write(letter)
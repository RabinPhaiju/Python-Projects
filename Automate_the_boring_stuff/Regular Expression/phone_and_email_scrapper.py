import re
import pyperclip

# python3
# todo: Create a regex for phone numbers
# 415-555-0000, 555-0000, (415) 555-0000, 555, 0000 ext 12345, ext.12345, x12345
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # are code optional
(\s|-) # first seperator
\d\d\d # first 3 digits
-       # second seperator
\d\d\d\d# last 4 digits
(((ext(\.)|\s)|x) # extension word-part optiona
(\d{2,5}))? # exteions number-part optional
)
''', re.VERBOSE)
# todo: create a regex for email addresses
# something.+_@(\d{2,5}?.com
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part # plus means must appear 1 or more time
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)
# todo: get the text off the clipboard
text = pyperclip.paste()
# todo: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
'\n'.join(allPhoneNumbers)

allEmail = []
for email in extractedEmail:
    allEmail.append(email)
'\n'.join(allEmail)
result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmail)
# print(result)
# todo: copy the extracted email/phone to the clipboard
pyperclip.copy(result)
print('done')

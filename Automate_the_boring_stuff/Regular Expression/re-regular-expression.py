import re

# ----------------- SEARCH A PHONE NO -----------------
# OR ANY FORMAT EXPRESSION

# message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'
# phoneNoRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # phone no format

# single_search = phoneNoRegex.search(message) # for 1st phone no
# print(single_search.group())
#
# all_search = phoneNoRegex.findall(message) # for all phone no. in list
# print(all_search)

# ----------------------- Group Expression ----------------------
# message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'
# phoneNoRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# group_search = phoneNoRegex.search(message)
# print(group_search.group(1))
# print(group_search.group(2))

# -----------------------------------------------------------------
# message = 'Call me (415) 555-1011 tomorrow, or at (415) 555-9999'
# phoneNoRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# group_search = phoneNoRegex.search(message)
# print(group_search.group())

# ---------------- Pipe separate pattern ------------------------
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel') # if word doesnot exit -- there is error
# print(mo.group())














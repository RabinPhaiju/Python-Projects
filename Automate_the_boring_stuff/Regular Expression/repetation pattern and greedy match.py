# ------------------ Repetition in Regex Pattern and Greedy match -----------------------------------
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adventure of Batman')
# print(mo.group())
# mo = batRegex.search('The Adventure of Batwoman')
# print(mo.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d\-\d\d\d\d') # the 1st 3 digit can be in the text or can't be.
# mo = phoneRegex.search('My phone number is 415-555-1234 . call me tomorrow.')
# print(mo.group())
#
# batRegex = re.compile(r'Bat(wo)*man') # * means "wo" can appear more than 1 time or 0 time
# ----------------------------------- # + means "wo" must appear 1 or more time
# ----------------------------------- # ? means 1 or 0
# mo = batRegex.search('The Adventure of Batwowowoman')
# print(mo.group())
#
# haRegex = re.compile(r'(ha){3}?') # {3} means must have (ha) 3 times
# mo = haRegex.search('"hahaha" is laugh')
# print(mo.group())
#
# mulphone_Regix = re.compile(r'((\d\d\d-)?\d\d\d\-\d\d\d\d(,)?){3}')
# mo = mulphone_Regix.search('444-3434,123-123-1234,555-4444 is phone')
# print(mo.group())


# haRegex = re.compile(r'(ha){3,5}') # {3,5} means must have (ha) 3-5 times # ---- greedy match------
# mo = haRegex.search('"hahahahaha" is laugh')
# print(mo.group())

# haRegex = re.compile(r'(ha){3,5}?') # {3,5}? means must have (ha) 3-5 times # ---- non-greedy match------
# mo = haRegex.search('"hahahahaha" is laugh')
# print(mo.group())
#
# haRegex = re.compile(r'(ha){3,}') # {3,} means must have (ha) more than 3-times
# mo = haRegex.search('"hahahahahahahahaha" is laugh')
# print(mo.group())


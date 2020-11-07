import re
# resume = '234-456-3443 is 334-444-3333'
# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneRegex.findall(resume))
#
# phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# print(phoneRegex.findall(resume))
#
# phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# print(phoneRegex.findall(resume))

# -------------------------- character class -----------------
# \d           any numeric digit from 0 to 9
# \D           any character that is not a numeric digit from 0 to 9
# \w           any letter,numeric digit, or the underscore character
# \W           any character that is not a letter, numeric digit, or that underscore character.
# \s           any space , tab, or new line character.
# \S           any character that is not a space, tab or newline.

# ---------------------------------------------------
# \d      One digit
# \d?      0 or 1 digit
# \d*       0 or more digit
# \d+       1 or more digit
# \d{3}     exactly 3 digit
# \d{3,5}   btwn 3 and 5 digit
# \d{3,}    3 or more digits

# ---------------------------------------------------


# lyrics = '12 drummers hello, 11 pipers hello, 10 lords hello'
# xmasRegex = re.compile(r'(\d+)\s(\w+)')
# print(xmasRegex.findall(lyrics))

# vowelRegex = re.compile(r'[aeiouAEIOU]') # [aeiou] == a|e|i|o|u ----- [a-z] == a to z
# print(vowelRegex.findall('Robocop eats baby foods.'))

# vowelRegex = re.compile(r'[aeiouAEIOU]{2}') # 2 times in a row
# print(vowelRegex.findall('Robocop eats baby foods.'))

# vowelRegex = re.compile(r'[^aeiouAEIOU]') # ^ not in [aeiousAEIOU]
# print(vowelRegex.findall('Robocop eats baby foods.'))





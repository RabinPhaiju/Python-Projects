import re

# namesRegex = re.compile(r'Agent \w+') # agent and word after agent till "space"
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))


# find and substitute
# print(namesRegex.sub('falana','Agent Alice gave the secret documents to Agent Bob.'))
#
# namesRegex = re.compile(r'Agent (\w)\w*')
# print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
#
# print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))


# ----------------------------- verbose ----------------

phoneRegex = re.compile(r'''
\d\d\d # area code
-       # space
\d\d\d  # first 3 digit
-       # space
\d\d\d\d# last 4 digit
''', re.VERBOSE | re.DOTALL | re.IGNORECASE) # bitwise or operator.










import re

# beginWithHelloRegex = re.compile(r'^Hello')
# print(beginWithHelloRegex.search('Hello there!'))
# print(beginWithHelloRegex.search('he said hello world')) # == None


# endsWithWorldRegex = re.compile(r'world!$') # $ means at the last
# print(endsWithWorldRegex.search('Hello world!'))


# allDigitsRegex= re.compile(r'^\d+$') # begins and ends with
# print(allDigitsRegex.search('2345654323456'))
# print(allDigitsRegex.search('23456 n 23456'))


# atRegex = re.compile(r'.at') # . means the word with "." and 2nd and 3rd letter is "at"
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#
# atRegex = re.compile(r'.{1,2}at') # .{1,2} means the word with "." 1 or 2 letter and 2nd and 3rd letter is "at"
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))


# name = 'First Name: Ali Last Name: Sweigart'
# nameRegex = re.compile(r'First Name: (.*?) Last Name: (.*)')
# print(nameRegex.findall(name))


# serve = '<To serve humans> for dinner.'
# nongreedy = re.compile(r'<(.*?)>')
# print(nongreedy.findall(serve))


# prime = 'Serve the public trust. \n New line \n Upload the law.'
# dotstar = re.compile(r'.*') # find all letter till new line (\n)
# print(dotstar.search(prime))
#
# dotstar = re.compile(r'.*', re.DOTALL) # find all letter even new line (\n)
# print(dotstar.search(prime))




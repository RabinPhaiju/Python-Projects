text = 'Hello-world'

# ---------------------------------------
print(text.isalpha())
print(text.isalnum())
print(text.isnumeric())
print(text.isspace())
print(text.istitle())

print(text.startswith('H'))
print(text.endswith('d'))

print(' , '.join(['1', '2', '3', '4']))

print('hello'.rjust(10, '*'))
print('hello'.ljust(10,'*'))
print('hello'.center(20,'='))

# ---------------------------------------
# print(text[:5])

# for char in text:
#     print(char)

# .count()
# print(text.count('Hello'))

# .split()
# print(text.split('-'))
# print(text.split('l'))

# text = input("Enter a stirng:")
# print(text.split(' '))

# .startwith()/endwith()
# print(text.startswith('Hello')) # returns true or false
# print(text.endswith('asd'))
# print(text.endswith('rld'))

# repeating strings
# print(text * 5)
# print(f'sir {text}' * 10)


# replacing strings
# print(text.replace('Hello', 'Bye'))
# a = 123456
# print(str(a).replace('1', 'a'))


# upper() lower()
# print(text.upper())


# strip() lstrip() rstrip()
# text = ' some text      '
# print(len(text.strip()))
# print(len(text.rstrip()))
# print(len(text.lstrip()))

# join()

# some_arr = ['This', 'Is', 'A ', 'Test', 'String']
# print('\n'.join(some_arr))

# reverse string
# print(text[::-1])
















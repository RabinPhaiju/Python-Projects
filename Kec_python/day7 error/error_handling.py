a = 10
b = 0

# try:
#     print(a / b)
# except: # run on if any error
#     print('error')
# else: # except->else    # runs on no error
#     print('No errors')
# finally: # Run even with error and not error
#     print('Finally')

# b = 'a'

# catch exception

# try:
#     print(a / b)
# except Exception as e:
#     print(e)


# specified error ---- and -- multile exception catch

# try:
#     print(a / b)
# except ZeroDivisionError:
#     print('0 le div nagara na')
# except Exception as e:
#     print(e)


# Raised custom error

# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     raise ZeroDivisionError('0 le divide nagara na')
# can be used if the program is long, and to find where the error is


# num1 = int(input('enter a number'))
# if num1 == 0:
#     raise ZeroDivisionError('B is zero')
# used in test cases, and if user don't provide input


# assert b != 0, 'B is zero'

# raise ZeroDivisionError('zero') # raise exceptionClass('error message')


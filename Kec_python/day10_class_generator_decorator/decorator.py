def decorator_fun(func):
    def inner_fun():
        print('function is decorated')
        func()
    return inner_fun


# @decorator_fun
def display():
    print('hello world')


# decorated = decorator_fun(display) # without @decorator_fun label
# decorated()

# display() # commented with @decorator_fun


# ----------------------decorator--------------------------------
def check_even(func):
    def inner_fun(*args, **kwargs):
        if args[0] % 2 == 0: # can be used loop for args
            func('even')
        else:
            func('odd')
    return inner_fun


def display1(a):
    print(a)


# ch_fun = check_even(display1)
# ch_fun(7)


@check_even # display2 is passed
def display2(a):
    print(a)


display2(2, 5, 3)
# display2(3435)









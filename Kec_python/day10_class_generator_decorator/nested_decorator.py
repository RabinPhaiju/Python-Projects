def dash(func):
    def inner_fun(*args, **kwargs):
        print('-'*10)
        func(*args, **kwargs)
        print('-'*10)
    return inner_fun


def check_even(func):
    def inner_fun(*args, **kwargs):
        for i in args:
            if i % 2 == 0: # can be used loop for args
                func('even')
            else:
                func('odd')
    return inner_fun


@dash
@check_even
def display(a):
    print(a)


# display = dash(check_even(display))
display(2, 5, 6, 8, 4, 5)






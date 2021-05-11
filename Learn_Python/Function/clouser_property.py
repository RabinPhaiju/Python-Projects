# hoc
def display(to_display):
    def inner_func():
        print('this is the value to print: ', to_display)
    return inner_func


hello = 'hello world'
can_print = display(hello)
can_print()


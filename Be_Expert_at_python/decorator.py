from time import time

def ntimes(n):
    def timer(func):
        def f(*args, **kwargs):
            before = time()
            for _ in range(n):
                print('running {.__name__}'.format(func))
            rv = func(*args, **kwargs) # func is add function
            after = time()
            print('elapsed = ', after-before)
            return rv
        return f
    return timer


@ntimes(2)
def add(*args, **kwargs):
    return args[0] + args[1]

@ntimes(2)
def sub(*args, **kwargs):
    return args[0] - args[1]



print('add(2, 20)', add(2, 20))
print('add(2, 3)', add(2, 3))
print('add(a + b)', add('a', 'b'))
print('sub(3, 2)', sub(3, 2))
# prime number check
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(100):
    print(is_prime(i), end=' ')


print('\n')


#None
def functions():
    return

print(functions())


def functions1():
    pass

print(functions1())
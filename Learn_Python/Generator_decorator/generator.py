# fibonacci


def fibo():
    x, y = 0, 1
    while True:
        yield x
        x, y = y , x + y # same line ma x change paxi matra hunxa


fibonacci = fibo()
print([next(fibonacci) for i in range(10)])
# for i in fibonacci: # infinite
    # print(next(fibonacci), end=' ')



# ----------generator comprehension -square------
# ()
sqr_num = (i**2 for i in range(100))
for i in range(10):
    print(next(sqr_num))


# ------------- Iter() ---------------------

s = 'hello'

s = iter(s)

print(next(s))

# class -------- generator ------------------------
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    # print(i)
    pass
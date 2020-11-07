from time import sleep
# top-level syntax, function -> underscore method

class compute:
    def __call__(self):
        rv = []
        for i in range(100):
            sleep(.5)
            print(i)
            rv.append(i)
        return rv


compute1 = compute()
# compute1()

# -----------------------------------------------
class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last +=1
        if self.last >10:
            raise StopIteration
        sleep(.5)
        return rv

# compute2 = Compute()
# for val in compute2:
#     print(val)
# dont load in memeory , so to save memory

# ----------------------
def fun():
    for i in range(10):
        sleep(.5)
        yield i
        

func = fun()
for i in range(10):
    print(next(func))


    
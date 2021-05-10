# some behaviour that I want to implement -> write some__function__
# top-level function or top-level syntax -> corresponding__
# x + y  -> __add__
# init x -> __init__
# repr(x)

class Polynomial:
    def __init__(self, *args):
        self.coeffs = args
    
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)# !r repr

    # def __str__(self):
    #     return 'hello'
            
    def __add__(self, other):
        return Polynomial(*(x for x in other.coeffs))
        
    def __len__(self):
        return len(self.coeffs)

    
        
p1 = Polynomial(2, 3, 4)
p2 = Polynomial(3, 4, 2)
print(len(p1))
print(p1)



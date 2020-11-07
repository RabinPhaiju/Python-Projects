class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def abs_value(self):
        return (self.real**2 + self.img**2)**0.5

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __str__(self):
        return '{} + {}i'.format(self.real, self.img)


c1 = Complex(2, 3)
c2 = Complex(4, 5)
# print(c1.abs_value())
print(c1 + c2)


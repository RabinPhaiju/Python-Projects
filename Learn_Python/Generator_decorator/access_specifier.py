# everything is public in python

class Parent:
    def __init__(self, x, y, z):
        self.__x = x # private
        self._y = y # protected
        self.z = z # public

    def view(self):
        print(f"{self.__x}, {self._y}, {self.z}")


class Child(Parent):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


p = Parent(1, 2, 3)
p.view()

c = Child(3, 4, 5)
c.view()


print(p._Parent__x) # private is used by _Parent__x
print(p._y) # protected is used by _y
print(p.z)

print(' ')
print(c._Parent__x)
print(c._y)
print(c.z)

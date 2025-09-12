# functions in class are called methods
# everything in python in object
# class is the blue-p rint


class Person:
    name = None # class variable / attributes
    age = None
    __salary = 70000 # private variable

    def __init__(self, name, age):
        # __ double Underscore are dunder methods
        self.name = name # instance variable
        self.age = age

    def describe(self): # methods
        print(self.name, self.age)

    def speak(self, to_speak): # methods
        print("{} says {}".format(self.name, to_speak))

    def __add__(self, other): # operator overriding
        # __ double Underscore are dunder methods
        return self.age + other.age

    def __private_function(self): # private function
        print('this is private', self.__salary)

    def take_private(self):
        self.__private_function()

    # name = 'asdf'
    # @staticmethod
    # def change_name(new_name): # change value of all object
    #     Person.name = new_name

    # class method
    @classmethod
    def change_name2(cls, new_name):
        return cls(new_name, 9999)


p1 = Person('rabin', 23) # instanciate
p2 = Person('sabin', 33)

p1.take_private()

# -----------------introspection--------------------
# checks if what is in the class that can be accessed
print(dir(p1))


# p1 = Person()
# Person.change_name('sabin')

p3 = Person.change_name2('new name')
print(p3.age)


p1.describe()
print(p1.name)

# p1.speak is override to string. Dont do it.
# p1.speak = 'speak'
# print(p1.speak)

p1.speak('hello')

print(p1 + p2) # call __add__operator

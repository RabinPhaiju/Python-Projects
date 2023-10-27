class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and {self.age} years old")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("meow")


class Dog(Animal):
    def speak(self):
        print("brak")


d1 = Dog('john', 2)
c1 = Cat('kale', 3, 'black')

d1.speak()

# Person ->Student
#         ->Worker
#                 ->Teacher


class Person:
    name = None # class variable / attributes
    age = None

    def describe(self): # methods
        print(self.name, self.age)

    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age

    def speak(self, to_speak): # methods
        print("{} says {}".format(self.name, to_speak))

    def __add__(self, other): # operator overriding
        return self.age + other.age


class Student(Person):
    # level = None # not necessary if constructor added it

    def __init__(self, name, age, level):
        super().__init__(name, age)
        # self.name = name # already written in parent class
        # self.age = age
        self.level = level

    def describe(self): # override of parent class---------------------------
        # super().describe() # to call super class/parent class method named describe
        print(f'{self.name} is {self.age} and in {self.level}')


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) # uses super class constructor to assign value, no repeat code
        self.salary = salary

    def describe(self):
        print(f'{self.name} is {self.age} years old and have {self.salary}')

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary


class Teacher(Worker):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary) # uses super class constructor to assign value, no repeat code
        self.subject = subject

    def describe(self):
        print(f'{self.name} is {self.age} years old and have {self.salary} and teaches {self.subject}')


s1 = Student('rabin', 23, 12)
print(s1.name)
s1.describe()


w1 = Worker('sabin', 34, 5666)
w1.describe()

t1 = Teacher('ram', 34, 45454, 'micro')
t2 = Teacher('rama', 34, 45454, 'microa')
t1.describe()

print(t1 + t2) # uses super class method
print(t1 > t2)
print(t1 >= t2)
print(t1 == t2)
print(t1 < t2)
print(t1 <= t2)

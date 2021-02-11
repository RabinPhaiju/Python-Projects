# 1. Create a class named 'Circle' with an attribute 'radius' and two methods that
# returns area and perimeter of the circle respectively.


# class Circle:
#     radius = None
#
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return (self.radius**2)*3.14
#
#     def perimeter(self):
#         return 2*3.14*self.radius
#
#
# c1 = Circle(4)
# print(c1.area())
# print(c1.perimeter())


# 2. Create a class name 'Vehicle' with attributes 'name', 'speed' and 'manufacturer'
# and a method to get the speed. Further extend this class into two other classes named 'Car'
# and 'Plane' with car having attributes 'horsepower' for 'Car' and 'engines' for 'Plane'.
# Use constructors to initialize the initial values.


# class Vehicle:
#     name = None
#     speed = None
#     manufacturer = None
#
#     def __init__(self, name, speed, manufacturer):
#         self.name = name
#         self.speed = speed
#         self.manufacturer = manufacturer
#
#     def get_speed(self):
#         return self.speed
#
#
# class Car(Vehicle):
#     horsepower = None
#
#     def __init__(self, name, speed, manufacturer, horsepower):
#         super().__init__(name, speed, manufacturer)
#         self.horsepower = horsepower
#
#     def get_car_detail(self):
#         return Car(self.name, self.speed, self.manufacturer, self.horsepower)
#
#     def print_car_detail(self):
#         print(f'Name is {self.name} , speed is {self.speed}, manufacture is {self.manufacturer} and horsepower is {self.horsepower}')
#
#
# class Plane(Vehicle):
#     engines = None
#
#     def __init__(self, name, speed, manufacturer, engines):
#         super().__init__(name, speed, manufacturer)
#         self.engines = engines
#
#     def get_plane_detail(self):
#         return Car(self.name, self.speed, self.manufacturer, self.engines)
#
#     def print_plane_detain(self):
#         print(f'Name is {self.name} , speed is {self.speed}, manufacture is {self.manufacturer} and horsepower is {self.engines}')
#
#
# c1 = Car('Toyota', 34, 2006, 'super engine')
# p1 = Plane('Boying', 45, 2005, 'super jet engine')
#
# print(c1.get_car_detail().name)
# c1.print_car_detail()
#
# p1.print_plane_detain()


# 3. Write a class with that has an attribute which stores a multi word string,
#  and a method that gives that string in reverse order word-by-word
# e.g. 'This is a test'
# output: 'test a is This'


class String:
    string = list()

    def reverse_string(self, li):
        self.string = li.split(' ')
        self.string.reverse()
        return self.string


s1 = String()
print(s1.reverse_string('This is a test'))










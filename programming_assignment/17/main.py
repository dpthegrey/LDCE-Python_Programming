"""
you can use + operator for adding numbers and at the same time to 
concatenate strings. It is possible because + operator is overloaded by both 
int class and str class. The operators are actually methods defined in respective classes. 
Defining methods for operators is known as operator overloading. 
For e.g: To use + operator with custom objects  you need to define a method called __add__.
"""
import math


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)

    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius

    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius

    def __str__(self):
        return "Circle with radius " + str(self.__radius)


c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c2.getRadius())

c3 = c1 + c2  # This became possible because we have overloaded + operator by adding a    method named __add__
print(c3.getRadius())

print(c3 > c2)  # Became possible because we have added __gt__ method

print(c1 < c2)  # Became possible because we have added __lt__ method

print(c3)  # Became possible because we have added __str__ method

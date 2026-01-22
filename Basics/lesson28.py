#Abstract Class and Duck Typing

from abc import ABC, abstractmethod
# ABC = Abstract Base Class
# abstractmethod = child class have to use

class Shape(ABC):  
    @abstractmethod
    def area(self):
        # This method MUST be implemented by child classes
        pass

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * self.radius ** 2

obj = Circle(5)

print(obj.area())

#Duck typing means polymorphism without inheritance
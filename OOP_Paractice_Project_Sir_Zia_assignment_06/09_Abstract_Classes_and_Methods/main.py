from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  

# Derived Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height  

# Creating an object of Rectangle class
rect = Rectangle(5, 3)
print(f"Area of Rectangle: {rect.area()}")  

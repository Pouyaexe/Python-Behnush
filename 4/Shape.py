import math

# Base class Shape
class Shape:
    def __init__(self, color: str):
        self.color = color
    
    def area(self):
        print("Subclasses must implement this method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Derived class Circle
class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Creating instances of Rectangle and Circle
rectangle = Rectangle("Red", 5.0, 3.0)
circle = Circle("Blue", 4.0)

# Demonstrating the usage of overridden methods
print(f"A {rectangle.color} rectangle with width {rectangle.width} and height {rectangle.height} has an area of {rectangle.area()}.")
print(f"A {circle.color} circle with radius {circle.radius} has an area of {circle.area()}.")
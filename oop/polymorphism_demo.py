# shape_classes.py

import math

# Base class
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)


# Example usage (for testing)
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    circle = Circle(7)

    print(f"Rectangle area: {rect.area()}")
    print(f"Circle area: {circle.area():.2f}")

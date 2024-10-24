# Factory Pattern Example in Python

"""
Factory Pattern

The Factory pattern provides a way to create objects without specifying the exact class of object that will be created.
It is used in complex situations where the type of the object required varies and needs to be specified in each case.

Why use Factory Pattern:
- When the type of objects required cannot be anticipated beforehand.
- When multiple objects that share similar characteristics need to be created.
- When you want to generalize the object instantiation process, since the object setup is complex in nature.
"""

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Factory class to create objects of different shapes
class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == 'CIRCLE':
            return Circle()
        elif shape_type == 'SQUARE':
            return Square()
        elif shape_type == 'RECTANGLE':
            return Rectangle()
        else:
            return None

# Usage
if __name__ == "__main__":
    # Create a factory
    factory = ShapeFactory()
    
    # Create a Circle object using the factory
    shape1 = factory.get_shape('CIRCLE')
    shape1.draw()  # Output: Drawing a Circle
    
    # Create a Square object using the factory
    shape2 = factory.get_shape('SQUARE')
    shape2.draw()  # Output: Drawing a Square
    
    # Create a Rectangle object using the factory
    shape3 = factory.get_shape('RECTANGLE')
    shape3.draw()  # Output: Drawing a Rectangle

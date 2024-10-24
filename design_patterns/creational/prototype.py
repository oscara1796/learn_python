# Prototype Pattern Example in Python

"""
Prototype Pattern

The Prototype pattern creates new objects by cloning existing ones.
It involves prototypal inheritance where a prototype object acts as a blueprint from which other objects inherit.

Why use Prototype Pattern:
- To avoid the overhead of creating complex objects from scratch.
- When instantiating a class is expensive or complicated.
- When you need to create a number of instances that share the same state or behavior.
"""

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

# Some class we want to clone
class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name}, {self.color}, {self.options}"

# Usage
if __name__ == '__main__':
    car = Car()
    print(car)
    prototype = Prototype()
    prototype.register_object('skylark', car)
    # Clone the object and update its attributes
    car_clone = prototype.clone('skylark', color="Blue")
    print(car_clone)
    # Output: Skylark, Blue, Ex

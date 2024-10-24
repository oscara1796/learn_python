# Constructor Pattern Example in Python

"""
Constructor Pattern

The Constructor pattern is a class-based pattern that uses the constructors present in the class to create specific types of objects.
It allows creating multiple instances of the same template, where instances can share methods but have different properties.

Why use Constructor Pattern:
- When you want to create multiple instances of the same template.
- Useful in designing libraries and plugins where objects need to share common methods but have different attributes.
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"The {self.name} says {self.sound}")

# Create multiple instances of Animal
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")
cow = Animal("Cow", "Moo")

# Usage
dog.make_sound()  # Output: The Dog says Woof
cat.make_sound()  # Output: The Cat says Meow
cow.make_sound()  # Output: The Cow says Moo

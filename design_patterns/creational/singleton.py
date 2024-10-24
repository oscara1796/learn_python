# Singleton Pattern Example in Python

"""
Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
This is useful when exactly one object is needed to coordinate actions across a system.

Why use Singleton Pattern:
- When you need to control access to a shared resource.
- Useful in logging, driver objects, caching, thread pool, configuration settings, etc.
"""

class Singleton:
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # If instance doesn't exist, create one
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True

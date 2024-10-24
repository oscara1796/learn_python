# Flyweight Pattern Example in Python

"""
Flyweight Pattern

The Flyweight pattern reduces the cost of creating and manipulating a large number of similar objects.
It does so by sharing as much data as possible among these objects, known as intrinsic state.

Real-life example:
In a text editor, each character can be represented as an object.
Instead of creating a separate object for each character (which is memory-intensive),
the Flyweight pattern allows sharing of character objects.

Components:
- Flyweight: The shared object that can be used in multiple contexts simultaneously.
- Flyweight Factory: Creates and manages flyweight objects.
"""

class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, intrinsic_state):
        # Returns a shared flyweight object
        if intrinsic_state not in self._flyweights:
            self._flyweights[intrinsic_state] = Flyweight(intrinsic_state)
        return self._flyweights[intrinsic_state]

class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state  # Shared state

    def operation(self, extrinsic_state):
        # Uses both intrinsic and extrinsic state
        print(f"Intrinsic State: {self.intrinsic_state}, Extrinsic State: {extrinsic_state}")

# Usage
if __name__ == "__main__":
    factory = FlyweightFactory()

    flyweight_a = factory.get_flyweight("A")
    flyweight_a.operation("First Call")

    flyweight_b = factory.get_flyweight("B")
    flyweight_b.operation("Second Call")

    # Reuses the existing flyweight for "A"
    flyweight_a2 = factory.get_flyweight("A")
    flyweight_a2.operation("Third Call")

    # Check that flyweight_a and flyweight_a2 are the same object
    print(flyweight_a is flyweight_a2)  # Output: True

    # Output:
    # Intrinsic State: A, Extrinsic State: First Call
    # Intrinsic State: B, Extrinsic State: Second Call
    # Intrinsic State: A, Extrinsic State: Third Call
    # True

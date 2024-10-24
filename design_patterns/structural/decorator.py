# Decorator Pattern Example in Python

"""
Decorator Pattern

The Decorator pattern allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class.
It is useful for adhering to the Open/Closed Principle (open for extension, closed for modification).

Real-life example:
Suppose we have a simple coffee ordering system, and we want to add various add-ons like milk, sugar, or whip to the coffee.
Using the Decorator pattern, we can add these features to our coffee dynamically without changing the original Coffee class.
"""

from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 2  # base price of simple coffee

    def get_description(self):
        return "Simple coffee"

# Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        # Delegates call to the decorated coffee
        return self.decorated_coffee.get_cost()

    def get_description(self):
        # Delegates call to the decorated coffee
        return self.decorated_coffee.get_description()

# Concrete Decorators
class Milk(CoffeeDecorator):
    def get_cost(self):
        # Adds extra cost for milk
        return self.decorated_coffee.get_cost() + 0.5

    def get_description(self):
        # Adds milk to the description
        return self.decorated_coffee.get_description() + ", milk"

class Sugar(CoffeeDecorator):
    def get_cost(self):
        # Adds extra cost for sugar
        return self.decorated_coffee.get_cost() + 0.2

    def get_description(self):
        # Adds sugar to the description
        return self.decorated_coffee.get_description() + ", sugar"

class Whip(CoffeeDecorator):
    def get_cost(self):
        # Adds extra cost for whip
        return self.decorated_coffee.get_cost() + 0.7

    def get_description(self):
        # Adds whip to the description
        return self.decorated_coffee.get_description() + ", whip"

# Usage
if __name__ == "__main__":
    # Start with a simple coffee
    my_coffee = SimpleCoffee()
    print(f"Cost: ${my_coffee.get_cost()}, Description: {my_coffee.get_description()}")

    # Add milk
    my_coffee = Milk(my_coffee)
    print(f"Cost: ${my_coffee.get_cost()}, Description: {my_coffee.get_description()}")

    # Add sugar
    my_coffee = Sugar(my_coffee)
    print(f"Cost: ${my_coffee.get_cost()}, Description: {my_coffee.get_description()}")

    # Add whip
    my_coffee = Whip(my_coffee)
    print(f"Cost: ${my_coffee.get_cost()}, Description: {my_coffee.get_description()}")

    # Output:
    # Cost: $2, Description: Simple coffee
    # Cost: $2.5, Description: Simple coffee, milk
    # Cost: $2.7, Description: Simple coffee, milk, sugar
    # Cost: $3.4, Description: Simple coffee, milk, sugar, whip

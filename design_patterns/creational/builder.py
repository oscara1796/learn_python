# Builder Pattern Example in Python

"""
Builder Pattern

The Builder pattern is a creational design pattern that lets you construct complex objects step by step.
It allows you to produce different types and representations of an object using the same construction code.

Why use Builder Pattern:
- When you need to create a complex object.
- To isolate the construction of complex objects from their representation.
- When you want to construct objects that must allow different representations.
"""

# Product
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.doors} doors, {self.windows} windows and a {self.roof} roof."

# Builder Interface
class HouseBuilder:
    def build_walls(self):
        pass
    def build_doors(self):
        pass
    def build_windows(self):
        pass
    def build_roof(self):
        pass
    def get_house(self):
        pass

# Concrete Builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()
    
    def build_walls(self):
        self.house.walls = "Brick"
    
    def build_doors(self):
        self.house.doors = "Wooden"
    
    def build_windows(self):
        self.house.windows = "Double-glazed"
    
    def build_roof(self):
        self.house.roof = "Tile"
    
    def get_house(self):
        return self.house

# Director
class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        self._builder.build_roof()
        return self._builder.get_house()

# Usage
if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = HouseDirector(builder)
    house = director.construct_house()
    print(house)
    # Output: House with Brick walls, Wooden doors, Double-glazed windows and a Tile roof.

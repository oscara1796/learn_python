# Composite Pattern Example in Python

"""
Composite Pattern

The Composite pattern composes objects into tree structures to represent part-whole hierarchies.
It allows clients to treat individual objects and compositions of objects uniformly.

Real-life example:
A file system where files and directories are represented.
Directories can contain files or other directories, forming a tree structure.
"""

from abc import ABC, abstractmethod

# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + self.name)

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        # Adds a child component
        self.children.append(component)

    def remove(self, component):
        # Removes a child component
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + self.name)
        # Recursively display child components
        for child in self.children:
            child.display(indent + 2)

# Usage
if __name__ == "__main__":
    # Create the root directory
    root = Directory("root")

    # Create subdirectories
    bin_dir = Directory("bin")
    etc_dir = Directory("etc")
    home_dir = Directory("home")

    # Create files
    file_a = File("a.txt")
    file_b = File("b.txt")
    file_c = File("c.txt")

    # Build the tree structure
    bin_dir.add(file_a)
    etc_dir.add(file_b)
    home_dir.add(file_c)

    root.add(bin_dir)
    root.add(etc_dir)
    root.add(home_dir)

    # Display the file system hierarchy
    root.display()

    # Output:
    # root
    #   bin
    #     a.txt
    #   etc
    #     b.txt
    #   home
    #     c.txt

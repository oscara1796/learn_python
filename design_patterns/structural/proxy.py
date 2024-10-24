# Proxy Pattern Example in Python

"""
Proxy Pattern

The Proxy pattern provides a surrogate or placeholder for another object to control access to it.
It can add additional functionality when accessing an object, like lazy initialization, access control, etc.

Real-life example:
Suppose you have a large image that takes time to load.
Using a proxy, you can delay the loading of the image until it's needed.

Types of proxies:
- Virtual Proxy: Controls access to a resource that is expensive to create.
- Remote Proxy: Represents an object in a different address space.
- Protection Proxy: Controls access based on permissions.
"""

from abc import ABC, abstractmethod

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        # Simulate a resource-intensive operation
        print(f"Loading {self.filename} from disk...")

    def display(self):
        print(f"Displaying {self.filename}")

# Proxy
class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  # Delays loading

    def display(self):
        if self.real_image is None:
            # Creates the real object only when needed
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage
if __name__ == "__main__":
    # Client code works with the proxy
    image = ImageProxy("large_photo.jpg")

    # Image is not loaded yet
    print("ImageProxy created. Image not loaded yet.")

    # Image will be loaded and displayed now
    image.display()

    # Image is already loaded; subsequent calls won't load it again
    image.display()

    # Output:
    # ImageProxy created. Image not loaded yet.
    # Loading large_photo.jpg from disk...
    # Displaying large_photo.jpg
    # Displaying large_photo.jpg

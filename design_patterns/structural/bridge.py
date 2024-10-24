# Bridge Pattern Example in Python

"""
Bridge Pattern

The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.
It separates the interface from the implementation, allowing them to change independently.

Real-life example:
In a drawing application, shapes can be drawn in different rendering modes (vector or raster).
Using the Bridge pattern, you can change the rendering implementation without affecting the shapes.
"""

from abc import ABC, abstractmethod

# Implementor interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

# Concrete Implementors
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} with vector rendering.")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius} with raster rendering.")

# Abstraction
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # Delegates the drawing to the renderer
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

# Usage
if __name__ == "__main__":
    raster_renderer = RasterRenderer()
    vector_renderer = VectorRenderer()

    circle = Circle(vector_renderer, 5)
    circle.draw()  # Output: Drawing a circle of radius 5 with vector rendering.
    circle.resize(2)
    circle.draw()  # Output: Drawing a circle of radius 10 with vector rendering.

    circle_raster = Circle(raster_renderer, 3)
    circle_raster.draw()  # Output: Drawing a circle of radius 3 with raster rendering.

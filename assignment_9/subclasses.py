from shape3d import Shape3D
import math

class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3


class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def surface_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height


class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def surface_area(self) -> float:
        return 6 * self.side ** 2

    def volume(self) -> float:
        return self.side ** 3

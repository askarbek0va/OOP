import random
from subclasses import Sphere,Cylinder,Cube

def generate_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
    if shape_type == 'Sphere':
        return Sphere(radius=random.randint(1, 10))
    elif shape_type == 'Cylinder':
        return Cylinder(radius=random.randint(1, 10), height=random.randint(5, 20))
    elif shape_type == 'Cube':
        return Cube(side=random.randint(1, 10))


shapes = [generate_random_shape() for _ in range(10)]

for i, shape in enumerate(shapes, 1):
    print(f"Shape {i}: {type(shape).__name__}")
    print(f"  Surface Area: {shape.surface_area():.2f}")
    print(f"  Volume: {shape.volume():.2f}\n")


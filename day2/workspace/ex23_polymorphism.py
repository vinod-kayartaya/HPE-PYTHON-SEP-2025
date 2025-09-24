import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def shape_name(self): ...

    @property
    def color(self):
        return "white"

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def color(self):
        return "red"
    
    @property
    def area(self):
        return self.radius * self.radius * math.pi
    
    @property
    def shape_name(self): 
        return 'circle'
    
class Rectangle(Shape):
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
    
    @property
    def shape_name(self):
        return 'rectangle'
    
class Square(Rectangle):
    def __init__(self, side=1):
        super().__init__(side, side)
    
    @property
    def shape_name(self):
        return 'square'

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.base * self.height / 2.
    
    @property
    def shape_name(self):
        return 'triangle'
    

def print_shape_areas(shapes: list):
    for s in shapes:
        if isinstance(s, Shape):
            print(f'area of {s.color} {s.shape_name} is {s.area}')


class Sphere(Shape):

    @property
    def shape_name(self):
        return 'shpere'

    @property
    def area(self):
        return None

def main():
    shapes = [
        Sphere(),
        Circle(1.2),
        Triangle(1.2, 3.4),
        Rectangle(1.2, 3.4),
        Square(1.2),
        "hexagon",
        [10, 20]
    ]

    print_shape_areas(shapes)


if __name__ == '__main__':
    main()

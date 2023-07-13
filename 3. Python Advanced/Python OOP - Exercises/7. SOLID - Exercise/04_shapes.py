from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: int, perpendicular_height: int):
        self.base = base
        self.perpendicular_height = perpendicular_height

    def area(self):
        return (self.base * self.perpendicular_height) / 2


class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def area(self):
        return self.side * self.side


class AreaCalculator:
    def __init__(self, shapes):
        if not isinstance(shapes, list):
            raise AssertionError(f"`shapes` should be of type `list`.")

        self.shapes = shapes

    @property
    def total_area(self):
        return sum([shape.area() for shape in self.shapes])


all_shapes = [Rectangle(2, 3), Triangle(1, 6), Square(3)]
calculator = AreaCalculator(all_shapes)
print(f"The total area is: {calculator.total_area}")

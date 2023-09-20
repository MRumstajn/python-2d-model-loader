from enum import Enum

class ShapeType(Enum):
    RECT = 1
    CIRCLE = 2
    COMPLEX = 3


class Shape:
    def __init__(self, type: ShapeType) -> None:
        self.type = type


class Rect(Shape):
    def __init__(self, x, y, x2, y2, color: list[int, int, int]) -> None:
        super().__init__(ShapeType.RECT)

        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color
    

class Complex(Shape):
    def __init__(self, verticies: list[tuple[int, int]], color: list[int, int, int]) -> None:
        super().__init__(ShapeType.COMPLEX)

        self.verticies = verticies
        self.color = color


class Circle(Shape):
    def __init__(self, radius: int, centerX, centerY, color: list[int, int, int]) -> None:
        super().__init__(ShapeType.CIRCLE)

        self.radius = radius
        self.centerX = centerX
        self.centerY = centerY
        self.color = color
        
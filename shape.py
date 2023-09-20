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

    def get_vertex(self) -> list[tuple[int, int]]:
        return [
            (self.x, self.y), (self.x, self.y2),
            (self.x, self.y2), (self.x2, self.y2),
            (self.x2, self.y2), (self.x2, self.y),
            (self.x2, self.y), (self.x, self.y)
            ]
        
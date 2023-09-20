import pygame
from shape import Shape, ShapeType

class Renderer:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def render(self, shapes: list[Shape]):
        # set up pygame window
        pygame.init()
        display = pygame.display.set_mode((self.width, self.height))

        # main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # rendering
            display.fill((0, 0, 0))

            for shape in shapes:
                self.draw_shape(shape, display)

            pygame.display.flip()
        
    def draw_shape(self, shape: Shape, display):
        if shape.type == ShapeType.RECT:
            rect = (shape.x, shape.y, shape.x2, shape.y2)
            pygame.draw.rect(display, (shape.color[0], shape.color[1], shape.color[2]), rect)

        elif shape.type == ShapeType.CIRCLE:
            pygame.draw.circle(display, (shape.color[0], shape.color[1], shape.color[2]), (shape.centerX, shape.centerY), shape.radius)

        elif shape.type == ShapeType.COMPLEX:
            pygame.draw.lines(display, (shape.color[0], shape.color[1], shape.color[2]), True, shape.verticies)
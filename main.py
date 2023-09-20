from pymodel_loader import ModelLoaader
from renderer import Renderer

loader = ModelLoaader()

shapes = []
for shape in loader.parse_file("shapes.json"):
    if shape == None:
        continue

    shapes.append(shape)

renderer = Renderer(300, 300)
renderer.render(shapes)
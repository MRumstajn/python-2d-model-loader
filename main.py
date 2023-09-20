from pymodel_loader import ModelLoaader
from shape import ShapeType

loader = ModelLoaader()

print("x,y   x2,y2   color")
for shape in loader.parse_file("shapes.json"):
    if shape == None:
        continue
    
    if shape.type == ShapeType.RECT:
        print(f"{shape.x}   {shape.y}   {shape.x2}   {shape.y2}   {shape.color[0]},{shape.color[1]},{shape.color[2]}")
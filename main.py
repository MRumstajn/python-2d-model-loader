from pymodel_loader import ModelLoaader
from shape import ShapeType, Rect, Complex

loader = ModelLoaader()

print("x,y   x2,y2   color")
for shape in loader.parse_file("shapes.json"):
    if shape == None:
        continue

    print(f"shape type: {shape.type}\n")

    if shape.type == ShapeType.RECT:
        print("start and end verticies:\n")
        print(f"{shape.x}   {shape.y}   {shape.x2}   {shape.y2}   {shape.color[0]},{shape.color[1]},{shape.color[2]}")

    elif shape.type == ShapeType.COMPLEX:
        print("verticies:\n")
        for vertex in shape.verticies:
            print(vertex)

    elif shape.type == ShapeType.CIRCLE:
        print("radius: " + str(shape.radius))
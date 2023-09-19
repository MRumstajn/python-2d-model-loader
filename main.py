from pymodel_loader import ModelLoaader

loader = ModelLoaader()

print("x,y   x2,y2   color")
for rect in loader.parse_file("rects.pyobj"):
    print(f"{rect.x}   {rect.y}   {rect.x2}   {rect.y2}   {rect.color[0]},{rect.color[1]},{rect.color[2]}")
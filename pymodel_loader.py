from shape import Rect, Shape
import json

MODEL_TYPES = ["rect", "circle", "complex"]

class ModelLoaader:
    def validate_shape_common(self, meta: dict):
        # check type tag
        if not "shape_type" in meta:
            return None
        
        if not meta["shape_type"] in MODEL_TYPES:
            return None
        
        # check required fields based on type
        if meta["shape_type"] == "rect":
            return self.validate_rect(meta)
        
        elif meta["shape_type"] == "complex":
            if not "verticies" in meta:
                return None
            
            if len(meta["verticies"]) == 0:
                return None
            
            return self.validate_complex(meta)
        
        elif meta["shape_type"] == "circle":
            if not "radius" in meta:
                return False
            
            return self.validate_circle()
        
        

    # TODO add support for multiple objects in one file
    def parse_file(self, file) -> list[Shape]:
        shapes = []
        with open(file, "r") as model_file:
            try:
                jsn = json.load(model_file)
            except:
                return []
            
            if not "shapes" in jsn:
                return []
            
            for shape_data in jsn["shapes"]:
                shapes.append(self.validate_shape_common(shape_data))

        return shapes
    
    def validate_rect(self, meta: dict) -> Rect:
        # validate verticies
        if not "verticies" in meta:
                return None
            
        if len(meta["verticies"]) != 2:
            return None
        
        # check if min and max vertex (x,y and x2,y2) overlap
        first_vertex = meta["verticies"]["0"]
        second_vertex = meta["verticies"]["1"]

        if self.are_vertecies_overlaping(first_vertex, second_vertex):
            return None

        # validate both ver
        if not self.validate_verticies(meta["verticies"]):
            return None
            
        # validate color
        if not "color" in meta:
            return None
        
        color: list[int] = meta["color"]
        
        if not self.validate_color(color):
            return None
        
        return Rect(first_vertex[0], first_vertex[1], second_vertex[0], second_vertex[1], color)
    
    def are_vertecies_overlaping(self, v1: tuple[int, int], v2: tuple[int, int]) -> bool:
        return v1[0] >= v2[0] and v1[1] >= v2[1]

    def validate_verticies(self, verticies: dict[str:list[int]]) -> bool:
        for key in verticies:
            if not self.validate_vertex(verticies[key]):
                return False
            
        return True
            
    def validate_vertex(self, vertex: list[int]) -> bool:
        return len(vertex) == 2 and type (vertex[0]) is int and type(vertex[1]) is int
    
    def validate_circle(self, meta: dict):
        pass

    def validate_complex(self, meta: dict):
        pass

    def validate_color(self, arr: list[int]) -> bool:
        # check r, g, b values range
        r, g, b = arr[0], arr[1], arr[2]
        if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
            return False
        
        return True
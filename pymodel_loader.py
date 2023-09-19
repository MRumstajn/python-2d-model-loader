from rect import Rect

# type, x, y, x2, y2, r, g, b
MODEL_META_COUNT = 8
MODEL_TYPES = ["rect"]

class ModelLoaader:
    def validate_meta_elements(self, meta: list[str]) -> list:
        # check meta info count
        if len(meta) != MODEL_META_COUNT:
            return None
        
        # check model type
        if not meta[0] in MODEL_TYPES:
            return None
        
        # check if x, y, x2, y2, r, g, b are integers
        try:
            x = int(meta[1])
            y = int(meta[2])
            x2 = int(meta[3])
            y2 = int(meta[4])
            r = int(meta[5])
            g = int(meta[6])
            b = int(meta[7])
        except ValueError:
            return None
        
        # check x, y, x2, y2 overlap
        if x >= x2 or y >= y2:
            return None

        # check r, g, b values range
        if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
            return None
        
        return [meta[0], x, y, x2, y2, r, g, b]

    def parse_file(self, file) -> list[Rect]:
        rects = []
        with open(file, "r") as model_file:
            for line in model_file:
                meta_elements = line.split(",")
                parsed_meta = self.validate_meta_elements(meta_elements)
                if parsed_meta != None:
                    _, x, y, x2, y2, r, g, b = parsed_meta
                    rects.append(Rect(x, y, x2, y2, [r, g, b]))

        return rects
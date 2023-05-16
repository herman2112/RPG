from pytmx.util_pygame import load_pygame

class TileMap:
    def __init__(self, filename):
        self.filename = filename

    def load_tmx(self):

        # Loads map information into pygame
        file = load_pygame(self.filename)

        # Stores each tile for each layer, contains x and y postion of the layer and its surface
        layer_tiles = {}

        # Iterates through all layers
        for name in file.layernames:
            layer = file.get_layer_by_name(name)

            layer_tiles[name] = []
            for x, y, surface in layer.tiles():
                layer_tiles[name].append([x * 16, y * 16, surface])
        
        return layer_tiles
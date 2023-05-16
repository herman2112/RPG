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
                layer_tiles[name].append([x, y, surface])
        
        return layer_tiles





























"""class Tile(pygame.sprite.Sprite):
    
    Represents each individual tile as a sprite
    
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
    
    # Turns CSV file into python list of lists
    def read_csv(self, filename):
        map = []
        
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            
            for row in data:
                map.append(list(row))
        
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        
        x, y = 0, 0
        
        for row in map:
            x = 0
            
            for tile in row:
                if """
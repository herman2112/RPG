import pygame
import os
from .assets import get_assets

def render_village(screen):
    tile_map = get_assets.TileMap("views/assets/village/VILLAGE.tmx")

    layer_tiles = tile_map.load_tmx()

    for layer in layer_tiles:
        for tile in layer_tiles[layer]:
            screen.blit(tile[2], (tile[0]*16, tile[1]*16))
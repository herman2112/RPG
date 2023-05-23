import pygame

from assets.get_assets import TileMap


def render_village():
    tile_map = TileMap(r"../RPG/assets/village/VILLAGE.tmx")

    layer_tiles = tile_map.load_tmx()

    return layer_tiles
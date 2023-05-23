import pygame
from states.state import State
from views.village import render_village
class Village(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.map = render_village()

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, display):
        for layer in self.map:
            for tile in self.map[layer]:
                display.blit(tile["surface"], tile["coordinates"])
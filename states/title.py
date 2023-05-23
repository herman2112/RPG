from states.state import State
from states.village import Village
class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, delta_time, actions):
        if actions["start"]:
            new_state = Village(self.game)
            new_state.enter_state(g)
        self.game.reset_keys()

    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Demo", 20, self.game.game_width/2, self.game.game_height/2)
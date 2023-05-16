import Character
from views.village import render_village
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Highland')

class Game:
    def __init__(self, surface):
        self._surface = surface
    
    
    # Instance methods
    def quit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        
        return False
    
    def draw_scene(self, scene):
        if scene == "village":
            render_village(self._surface)

    

def main():
    
    print("The game is running!")
    game = Game(screen)
    
    while True:
        if game.quit_game():
            print("Game is quitting!")
            pygame.quit()
            quit()
        
        # LOGIC
        
        # DRAW
        game.draw_scene("village")
                
        pygame.display.update()
        

if __name__ == "__main__":
    main()
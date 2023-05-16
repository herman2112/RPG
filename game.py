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
    

def main():
    
    print("The game is running!")
    game = Game(screen)
    
    while True:
        if game.quit_game():
            print("Game is quitting!")
            pygame.quit()
            sys.exit()
        
        # LOGIC
        
        # DRAW
        screen.fill("black")
        render_village(screen)
                
        pygame.display.update()
        

if __name__ == "__main__":
    main()
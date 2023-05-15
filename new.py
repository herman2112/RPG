import Character
import pygame
import tkinter as tk
import sys

pygame.init()
clock = pygame.time.Clock()

tk_obj = tk.Tk()

screen_info = {
    'width': tk_obj.winfo_screenwidth(),
    'height': tk_obj.winfo_screenheight()
}

screen = pygame.display.set_mode((screen_info['width'], screen_info['height']))

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
    
    while 1:
        if game.quit_game():
            print("Game is quitting!")
            pygame.quit()
            quit()
        
        # LOGIC
        
        # DRAW
        

if __name__ == "__main__":
    main()
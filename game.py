import Character
import pygame
import tkinter as tk
import sys

class Game:
    def __init__(self, screen_width, screen_height, status = False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.status = status
    
    # Instance methods
    def run(self):
        pygame.init()
        
        self.status = True
        
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        clock = pygame.time.Clock()
        
        pygame.display.set_caption('jogo bom d+')
        
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    
            screen.fill("white")
            
            pygame.display.flip()
                
        pygame.quit()
        sys.quit()

    def quit(self):
        self.status = False
        return


def main():

    root = tk.Tk()
    
    game = Game(root.winfo_screenwidth(), root.winfo_screenheight())

    game.run()

if __name__ == '__main__':
    main()

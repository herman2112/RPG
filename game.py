import Character
import pygame
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
        pygame.display.set_caption('jogo bom d+')

    def quit(self):
        pygame.quit()
        sys.quit()


def main():

    game = Game(1280, 720)

    game.run()

    while game.status:
        pass

if __name__ == '__main__':
    main()

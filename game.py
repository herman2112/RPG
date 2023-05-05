import Character
import pygame
import sys

class Game:
    def __init__(self, screen_width, screen_height, status = False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.status = status
    
    # Class methods
    @classmethod
    def render_screen(cls, surf, color):
        pass

    # Instance methods
    def run(self):
        pygame.init()
        
        print("Game is running!")

        self.status = True
        
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        clock = pygame.time.Clock()
        
        pygame.display.set_caption('RPG nosso de cada dia')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
            screen.fill("white")

            # Game render here

            Game.render_screen()

            pygame.display.flip()

    def quit(self):
        self.status = False
        print("The game has quit!")
        pygame.quit()
        sys.quit()
        return


def main():

    #root = tk.Tk()
    
    game = Game(1280, 720)

    game.run()

if __name__ == '__main__':
    main()

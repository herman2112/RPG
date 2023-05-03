import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
running = True

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('jogo bom d+')

def main():

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()



        pygame.display.flip()
        pygame.time.delay(60)

if __name__ == '__main__':
    main()
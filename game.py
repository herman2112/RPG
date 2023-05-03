from Character import *
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


        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        ##player.move(dx, dy)
        pygame.display.flip()
        pygame.time.delay(60)

if __name__ == '__main__':
    main()

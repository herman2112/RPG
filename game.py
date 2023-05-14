import Character
import pygame
import tkinter as tk
import sys

pygame.init()
clock = pygame.time.Clock()

#tk_obj = tk.Tk()

'''screen_info = {
    'width': tk_obj.winfo_screenwidth(),
    'height': tk_obj.winfo_screenheight()
}'''

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Jogo bom :)')

warrior = pygame.image.load('assets/circle-41674.png')
warrior = pygame.transform.scale(warrior, (200, 200))
base_rectangle = warrior.get_rect()

vY = 5
vX = 5

class Game:
   def __init__(self, surface):
       self._surface = surface

def main():
    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #LOGIC
        key = pygame.key.get_pressed()

        if key[pygame.K_w] and base_rectangle.top > 0:
            base_rectangle.move_ip(0, -vY)
        
        if key[pygame.K_s] and 1280 - base_rectangle.top > 760:
            
            base_rectangle.move_ip(0, vY)

        if key[pygame.K_a] and base_rectangle.left > 0:
            base_rectangle.move_ip(-vX, 0)
        
        if key[pygame.K_d] and base_rectangle.left < 1080:
            print(f"w: {screen.get_width()}")
            print(f"dist: {base_rectangle.left}")
            base_rectangle.move_ip(vX, 0)

        #DRAW
        screen.fill((0, 0, 0))
        screen.blit(warrior, base_rectangle)
        pygame.display.update()
        clock.tick(60)



if __name__ == '__main__':
    main()

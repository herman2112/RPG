import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        heigth = image.get_heigth()
        self.image = pygame.transform.scale(image, (int(width * scale), int(heigth * scale)))
        self.react = self.image.get_react()
        self.react.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.react.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.react.x, self.react.y))

        return action
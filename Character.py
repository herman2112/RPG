import pygame
import sys

class Character():
    def __init__(self, x, y, image_path, name, Hp, Atk, Def, Spd, Xp, Estado):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.name = name
        self.font = pygame.font.Font(None, 24)
        self.Hp = 100
        self.Atk = 10
        self.Def = 10
        self.Spd = 3
        self.Xp = 0
        self.Estado = True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        text = self.font.render(self.font, True, (0,0,0))
        text_rect = text.get_rect(center=(self.x + self.image.get_width() // 2, self.y - 20))
        screen.blit(text, text_rect)
    
    def attack(self, other):
        other.Hp -= self.Atk

    

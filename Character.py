import pygame
import sys

class Character():
    def __init__(self, x, y, image_path, name, Hp = 100, Atk = 5, Def = 5, Spd = 3, Xp = 0, Stm = 100, Estado = True):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.name = name
        self.font = pygame.font.Font(None, 24)
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Spd = Spd
        self.Xp = Xp
        self.Stm = Stm
        self.Estado = Estado

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        text = self.font.render(self.font, True, (0,0,0))
        text_rect = text.get_rect(center=(self.x + self.image.get_width() // 2, self.y - 20))
        screen.blit(text, text_rect)

    def move(self, dx, dy):
        self.dx += dx * self.Spd
        self.dy += dy * self.Spd
    
    def attack(self, other):
        other.Hp -= self.Atk
        self.Stm -= 20

    
class Warrior(Character):
    def __init__(self, x, y, image_path, name, Hp = 150, Atk = 5, Def = 10, Spd = 2, Xp = 0, Stm = 100, Estado = True):
       pass 
    def fury(self, other):
        other.Hp -= self.Atk * 1.50
        self.Stm -= 50


class Wizard(Character):

    def __init__(self, x, y, image_path, name, Hp = 100, Atk = 8, Def = 6, Spd = 3, Xp = 0, Stm = 100, Estado = True):
        pass
    def BolaDeFogo(self, other):
        other.Hp -= 20
        self.Stm -= 55


class Rogue(Character):
    def __init__(self, x, y, image_path, name, Hp = 75, Atk = 5, Def = 5, Spd = 5, Xp = 0, Stm = 150, Estado = True):
        pass
    def BackStab(self,other):
        other.Hp -= self.Atk * 2.5
        self.Stm -= 45


class Orc(Character):

    def __init__(self, x, y, image_path, name, Hp = 150, Atk = 5, Def = 10, Spd = 2, Xp = 0, Stm = 100, Estado = True):
        pass
    def Porradao(self,other):
        other.Hp -= self.Atk *1.5
        self.Stm -= 50

class Dragao(Character):
    def __init__(self, x, y, image_path, name, Hp = 100, Atk = 8, Def = 6, Spd = 3, Xp = 0, Stm = 100, Estado = True):
        pass
    def BolaDeFogo(self, other):
        other.Hp -= 20
        self.Stm -= 55

class Goblin(Character):
    def __init__(self, x, y, image_path, name, Hp = 75, Atk = 5, Def = 5, Spd = 5, Xp = 0, Stm = 150, Estado = True):
        pass
    def BackStab(self,other):
        other.Hp -= self.Atk * 2.5
        self.Stm -= 45

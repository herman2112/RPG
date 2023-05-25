import pygame
import time

from states.title import Title

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.ENTER_KEY = False
        self.BACK_KEY = False

        self.screen_width, self.screen_height = 1280, 720
        self.game_width, self.game_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.game_height))
        self.game_canvas = pygame.Surface((self.game_width, self.game_height))
        self.font = pygame.font.get_default_font()

        self.actions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "action1": False,
            "action2": False,
            "start": False,
            "back": False
        }

        self.dt, self.prev_time = 0, 0
        self.white, self.black = (255, 255, 255), (0, 0, 0)

        self.state_stack = []
        
        self.load_states()
    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.check_events()
            self.update()
            self.render()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.actions["start"] = True
                
                if event.key == pygame.K_BACKSPACE:
                    self.actions["back"] = True
                
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                
                if event.key == pygame.K_s:
                    self.actions["down"] = True
                
                if event.key == pygame.K_d:
                    self.actions["right"] = True
                
                if event.key == pygame.K_a:
                    self.actions["left"] = True
                
                if event.key == pygame.K_p:
                    self.actions["action1"] = True
                
                if event.key == pygame.K_o:
                    self.actions["action2"] = True


    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()

        self.dt = now - self.prev_time
        self.prev_time = now

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, surface, text, size, x, y):
        font = pygame.font.Font(self.font, size)

        text_surface = font.render(text, True, self.black)

        text_rect = text_surface.get_rect()
        text_rect.center = x, y
        surface.blit(text_surface, text_rect)

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False

        self.UP_KEY = False
        self.DOWN_KEY = False
        self.ENTER_KEY = False
        self.BACK_KEY = False

        self.screen = pygame.display.set_mode((1280, 720))

        self.font = pygame.font.get_default_font()

        self.white, self.black = (255, 255, 255), (0, 0, 0)

    def game_loop(self):
        while self.playing:
            self.check_events()

            if self.ENTER_KEY:
                self.playing = False

            self.screen.fill(self.black)
            self.draw_text("Carlos Alberto!", 20, 1280/2, 720/2)
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True
                
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font, size)

        text_surface = font.render(text, True, self.white)

        text_rect = text_surface.get_rect()
        text_rect.center = x, y
        self.screen.blit(text_surface, text_rect)

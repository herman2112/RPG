import pygame
import Button

pygame.init()

##cria a tela
screen_width = 1240
screen_heigth = 720

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

##fonte do texto
font = pygame.font.SysFont("arialblack",20)
TEXT_COL = (255,255,255)

#load button images
resume_img = pygame.image.load("imagens/button_resume.png")
options_img = pygame.image.load("imagens/button_options.png")
quit_img = pygame.image.load("imagens/button_quit.png")
video_img = pygame.image.load("imagens/button_video.png")
audio_img = pygame.image.load("imagens/button_audio.png")
keys_img = pygame.image.load("imagens/button_keys.png")
back_img = pygame.image.load("imagens/button_back.png")

#create button instaces
resume_button = Button.Button(304, 125, resume_img, 1)
options_button = Button.Button(297, 250, options_img, 1)
quit_button = Button.Button(336, 375, quit_img, 1)
video_button = Button.Button(226, 75, video_img, 1)
audio_button = Button.Button(225, 200, audio_img, 1)
keys_button = Button.Button(246, 325, keys_img, 1)
back_button = Button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen.fill((52,78,91))

    ##check if game is paused

    if game_paused == True:
        #check menu state
        if menu_state == "main":
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False    
        #check if options menu is open
        if menu_state == "options":
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    #display menu
    else:
        draw_text("Precione ESPACO para pausar", font, TEXT_COL, 200, 290)
        #pass

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

import pygame
import Button

pygame.init()

##cria a tela
screen_width = 800
screen_heigth = 600

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Main Menu")


#game variables

game_paused = False

##fonte do texto
font = pygame.font.SysFont("ariablack",40)
TEXT_COL = (255,255,255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()

#crate button instaces
resume_button = Button.Button(304,125,resume_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
while run:

    screen.fill((52,78,91))

    ##check if game is paused

    if game_paused == True:
        resume_button.draw(screen)
    
    #display menu
    else:
        draw_text("Precione ESPACO para pausar", font, TEXT_COL, 200, 290)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
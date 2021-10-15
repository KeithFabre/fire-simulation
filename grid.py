import pygame
import numpy as np
from Button import button

# cores
silver = (255, 255, 255)
gold = (212, 175, 55)
black = (0, 0, 0)

brown = (150, 75, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
forest = (3, 124, 80)


width = 16  # largura célula
height = 16  # altura célula

margin = 1  # margem entre cada célula
n = 50 # número de linhas e colunas

win_dir = 'reset' # pegar direção com setas do teclado


terrain_size = [n,n]

total_time = 100
states = np.ones((total_time,*terrain_size))

pygame.init()

min_width = (width+margin)*n
min_height = (height+margin)*n
window_size = [min_width+1, min_height+175]
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption("Cenário Ambiental Inicial")


# load button image
exit_img = pygame.image.load('./Button/save.png').convert_alpha()

# create button instance
exit_button = button.Button(
    (window_size[0]/3 + window_size[0]/10), window_size[1]-window_size[0]/6, exit_img, 0.25)

done = False

new_color = green  # cor para a célula
clicked = 1  # valor para célula

clock = pygame.time.Clock()


def paintCell():
    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    col = pos[0] // (width + margin)
    row = pos[1] // (height + margin)

    outsideGrid = (pos[0] > (width+margin)*n) or (pos[1] > (height+margin)*n)

    outsideWindow = True if pygame.mouse.get_focused() == 0 else False

    if click[0] == True:
        if outsideGrid == False and outsideWindow == False:
            states[0][row][col] = clicked

while not done:

    screen.fill(silver)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.KEYDOWN:
            # vegetação rasteira
            if event.key == pygame.K_g:
                clicked = 1

            # fogo
            if event.key == pygame.K_r:
                clicked = 100

            # floresta
            if event.key == pygame.K_f:
                clicked = 10

            # aceiro e terra vazia
            if event.key == pygame.K_a:
                clicked = 0

            # preto -- área queimada
            if event.key == pygame.K_z:
                clicked = -1

            # água
            if event.key == pygame.K_b:
                clicked = -2
            
            # zona protegida -- o que queremos proteger
            if event.key == pygame.K_k:
                clicked = 2651
        
            # para direção do vento
            if event.key == pygame.K_RIGHT:
                win_dir = 'right'
                print('Direção do vento: {}'.format(win_dir))
            
            if event.key == pygame.K_LEFT:
                win_dir = 'left'
                print('Direção do vento: {}'.format(win_dir))
            
            if event.key == pygame.K_UP:
                win_dir = 'up'
                print('Direção do vento: {}'.format(win_dir))
            
            if event.key == pygame.K_DOWN:
                win_dir = 'down'
                print('Direção do vento: {}'.format(win_dir))


    for row in range(n):  # desenha a grid
        for col in range(n):

            color = green  # preenche de vegetação

            # água
            if states[0][row][col] == -2:
                color = blue

            # área queimada
            if states[0][row][col] == -1:
                color = black
            
            # aceiro ou terra
            if states[0][row][col] == 0:
                color = brown

            # vegetação
            if states[0][row][col] == 1:
                color = green

            # fogo
            if states[0][row][col] == 100:
                color = red

            # floresta
            if states[0][row][col] == 10:
                color = forest
            
            # zona protegida
            if states[0][row][col] == 2651:
                color = gold

            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*col + margin,
                              (margin+height)*row + margin,
                              width,
                              height])
    #save button
    if exit_button.draw(screen):
        done = True

    clock.tick(60)  # 60 frames/s

    paintCell()
    pygame.display.flip()  # updates screen


pygame.quit()

#print(states)


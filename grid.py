'''
    Inicia com grid em branco
    Ao clicar nas células é preenchida uma cor
    Se a tecla 'G' for pressionada, a cor é verde
    Se a tecla 'R' for pressionada, a cor é vermelha
    Se a tecla 'B' for pressionada, a cor é azul
    Se a tecla 'W' for pressionada, a cor é marrom

    Se a tecla 'X' for pressionada, o valor da célula é zerado
    e ela volta a ser branca

    Isso para definir os locais com vegetação, fogo, madeira e água
'''


import pygame
from Button import button




# cores
black = (0, 0, 0)
silver =(255, 255, 255) 
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
brown = (150, 75, 0)

width = 15 # largura célula
height = 15 # altura célula








margin = 3 # margem entre cada célula
n = 30  # número de linhas e colunas






grid = [] # grid inicia com 1s => para área arborizada
for row in range(n):
    grid.append([])
    for col in range(n):
        grid[row].append(1)

pygame.init()







window_size = [545,690]
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption("Grid 2D")





#load button image
exit_img = pygame.image.load('./Button/save.png').convert_alpha()

#create button instance
exit_button = button.Button((window_size[0]/3 + window_size[0]/20), window_size[1]-window_size[0]/4, exit_img, 0.25)





done = False



new_color = green # cor para a célula
clicked = 1 # valor para célula




clock = pygame.time.Clock()



while not done:

    screen.fill(silver)
    
    if exit_button.draw(screen):
        run = False

    for event in pygame.event.get():  

        if event.type == pygame.QUIT: 
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            col = pos[0] // (width + margin)
            row = pos[1] // (height + margin)

            grid[row][col] = clicked
            print("Click ", pos, "Grid coordinates: ", row, col)
        
        # tentando habilitar clique e arraste pra selecionar células
        if event.type == (pygame.MOUSEBUTTONUP):
            posMotion = pygame.mouse.get_pos()
            print('clicked and moved {}'.format(posMotion))

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_g:
                clicked = 1

            if event.key == pygame.K_r:
                clicked = 2

            if event.key == pygame.K_b:
                clicked = 3

            if event.key == pygame.K_w:
                clicked = 4

            if event.key == pygame.K_z:
                clicked = -1

            if event.key == pygame.K_x:
                clicked = 0
            


        
        
    
    for row in range(n): # desenha a grid
        for col in range(n):

            color = green # preenche de branco

            if grid[row][col] == -1:
                color = black
            if grid[row][col] == 1:
                color = green
            if grid[row][col] == 2:
                color = red
            if grid[row][col] == 3:
                color = blue
            if grid[row][col] == 4:
                color = brown
            if grid[row][col] == 0:
                color = white

            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*col + margin,
                              (margin+height)*row + margin,
                              width,
                              height])

    clock.tick(60) # 60 frames/s
    
    pygame.display.flip() # atualiza a tela


pygame.quit()

#print(grid)
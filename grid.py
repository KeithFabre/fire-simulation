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

# cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = 	(0, 0, 255)
brown = (150, 75, 0)

# largura e altura de cada grid
width = 25
height = 25

# margem entre cada célula
margin = 3

n = 15  # número de linhas e colunas

# cria um array 2D: lista de listas e inicia com zeros
grid = []
for row in range(n):
    grid.append([])
    for col in range(n):
        grid[row].append(0)

# inicializa o pygame
pygame.init()

# altura e largura da tela
window_size = [425, 425]
screen = pygame.display.set_mode(window_size)

# título da tela
pygame.display.set_caption("Grid 2D")

# loop até que user clique o botão para sair
done = False

# cor definida pelo usuário que preencherá célula
new_color = white
clicked = 0

# clock que será usado na execução
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():  # usuario fez algo
        
        if event.type == pygame.QUIT:  # se user clicou para sair
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # user clicou com o mouse: pega posição
            pos = pygame.mouse.get_pos()
            # muda as coordenadas x e y para coordenadas grid
            col = pos[0] // (width + margin)
            row = pos[1] // (height + margin)

            # define aquela localização como clicked
            grid[row][col] = clicked
            print("Click ", pos, "Grid coordinates: ", row, col)
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_g:
                clicked = 1
            
            if event.key == pygame.K_r:
                clicked = 2
            
            if event.key == pygame.K_b:
                clicked = 3

            if event.key == pygame.K_w:
                clicked = 4

            if event.key == pygame.K_x:
                clicked = 0

        # cor de fundo da tela
        screen.fill(black)

    # desenha a grid
    for row in range(n):
        for col in range(n):
            # preenche de branco inicialmente
            color = white

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
            
    
    # limita para 60 frames por segundo
    clock.tick(60)
    # atualiza a tela com o que foi desenhado
    pygame.display.flip()


pygame.quit()


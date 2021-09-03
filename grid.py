'''
    Inicia com grid em branco
    Ao clicar nas células é preenchida uma cor
    Se a tecla 'G' for pressionada, a cor é verde
    Se a tecla 'R' for pressionada, a cor é vermelha

    Isso para definir os locais com vegetação e fogo
'''


import pygame

# cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# largura e altura de cada grid
width = 20
height = 20

# margem entre cada célula
margin = 5

n = 20  # número de linhas e colunas

# cria um array 2D: lista de listas e inicia com zeros
grid = []
for row in range(n):
    grid.append([])
    for col in range(n):
        grid[row].append(0)


grid[1][5] = 1

# inicializa o pygame
pygame.init()

# altura e largura da tela
window_size = [500, 500]
screen = pygame.display.set_mode(window_size)

# título da tela
pygame.display.set_caption("Grid 2D")

# loop até que user clique o botão para sair
done = False

# cor definida pelo usuário que preencherá célula
new_color = white

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
            # define aquela localização como 1
            grid[row][col] = 1
            print("Click ", pos, "Grid coordinates: ", row, col)
        
        if event.type == pygame.KEYDOWN:

            # checa se tecla 'G' foi pressionada
            if event.key == pygame.K_g:
                new_color = green
            
            # checa se tecla 'R' foi pressionada
            if event.key == pygame.K_r:
                new_color = red
            
            # checa se tecla 'R' foi pressionada
            if event.key == pygame.K_w:
                new_color = white

        # cor de fundo da tela
        screen.fill(black)

    # desenha a grid
    for row in range(n):
        for col in range(n):
            color = white
            if grid[row][col] == 1:
                color = new_color
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


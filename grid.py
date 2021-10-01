import pygame
from Button import button

# cores
black = (0, 0, 0)
silver = (255, 255, 255)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
brown = (150, 75, 0)
gold = (212, 175, 55)

# the golden part will be the part we want to avoid burning
# like protected areas
# its value will be x, and if fire catches this area the 
# simulation stops


width = 15  # largura célula
height = 15  # altura célula

margin = 1  # margem entre cada célula
n = 40  # número de linhas e colunas


grid = []  # grid inicia com 1s => para área arborizada
for row in range(n):
    grid.append([])
    for col in range(n):
        grid[row].append(1)

pygame.init()

min_width = (width+margin)*n
min_height = (height+margin)*n

print(min_width,min_height)

window_size = [min_width+1, min_height+175]
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption("Grid 2D")


# load button image
exit_img = pygame.image.load('./Button/save.png').convert_alpha()

# create button instance
exit_button = button.Button(
    (window_size[0]/3 + window_size[0]/20), window_size[1]-window_size[0]/4, exit_img, 0.25)

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
            grid[row][col] = clicked


while not done:

    screen.fill(silver)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True


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
            
            if event.key == pygame.K_k:
                clicked = 'x'

            if event.key == pygame.K_x:
                clicked = 0

    for row in range(n):  # desenha a grid
        for col in range(n):

            color = green  # preenche de branco

            
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
            if grid[row][col] == 'x':
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

print(grid)


'''
    tirar probabilidade
    ajustar tamanho do terreno com tamanho da grid
    
    -ok- representar vegetação
    -- representar aceiro (terreno queimado após fogo passar)
    -- representar lagos
    -- representar madeira
    -- reduzir valor grid até chegar em 0 que é área queimada
    -- área branca (terra vazia, o que fazer?)


    -- incluir direção do vento
    -- parar quando chegar na zona dourada (se tiver uma)

    -- usar descida de gradiente pra alguma coisa?
    

'''

import numpy as np
import imageio
import grid

# 0 = clear, 1 = fuel, 2 = fire

terrain_size = [100, 100]

states = []
states = grid.grid[:]

print('--------COMEÇO--------------')
print(states)

total_time = 300

states = np.ones((total_time,*terrain_size))
states[0,terrain_size[0]//2,terrain_size[1]//2] = 2

found_protected = False # ends simulation if it gets to protected area


for t in range(1, total_time):
    states[t] = states[t-1].copy() # assume valor do estado anterior

    print(states[2])

    for i in range(1, terrain_size[0]-1): # anda por linhas
        for j in range(1, terrain_size[1]-1): # anda por colunas


            if states[t-1,i,j] == 100: # se no tempo anterior, nesse local havia fogo
                states[t,i,j] = 0 # apaga o fogo no tempo atual
            

                # checa se no tempo anterior, ao redor desse local,
                # havia combustível
                if states[t-1,i+1,j] == 1:
                    states[t,i+1,j] = 2
                if states[t-1,i-1,j] == 1:
                    states[t,i-1,j] = 2
                if states[t-1,i,j+1] == 1:
                    states[t,i,j+1] = 2
                if states[t-1,i,j-1] == 1:
                    states[t,i,j-1] = 2

print('--------FIM--------------')
print(states)
























'''for t in range(1,total_time):
    states[t] = states[t-1].copy()

    for x in range(1,terrain_size[0]-1):
        for y in range(1,terrain_size[1]-1):
            if states[t-1,x,y] == 2: # it's on fire
                states[t,x,y] = 0 # put it out and clear it

                # if there's fuel surrounding it: set it on fire
                if states[t-1,x+1,y] >= 1:
                    states[t,x+1,y] = 100
                if states[t-1,x-1,y] >= 1:
                    states[t,x-1,y] = 100
                if states[t-1,x,y+1] >= 1:
                    states[t,x,y+1] = 100
                if states[t-1,x,y-1] >= 1:
                    states[t,x,y-1] = 100
                
                # fazer lógica pra diminuir até chegar em 0
                # e assim passar pra próxima

                # if it gets to protected area: stop simulation
            
                












colored = np.zeros((grid.n, grid.n,3),dtype=np.uint8)

# Color
for t in range(states.shape[0]):
    for x in range(states[t].shape[0]):
        for y in range(states[t].shape[1]):
            value = states[t,x,y].copy()

            if value == 0:
                colored[t,x,y] = [139,69,19] # clear
            elif value == 1:
                colored[t,x,y] = [0,255,0] # fuel
            elif value == 2:
                colored[t,x,y] = [255,0,0] # burning

# Crop
cropped = colored[:200, 1:terrain_size[0]-1,1:terrain_size[1]-1]

imageio.mimsave('./video.gif', cropped)'''
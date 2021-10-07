import numpy as np
import imageio

# 0 = clear, 1 = fuel, 2 = fire


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
    

'''



prob = .6
total_time = 300
terrain_size = [100,100]

states = np.zeros((total_time,*terrain_size))
states[0] = np.random.choice([0,1],size=terrain_size,p=[1-prob,prob])
# set middle cell on fire
states[0,terrain_size[0]//2,terrain_size[1]//2] = 2

for t in range(1,total_time):
    states[t] = states[t-1].copy()

    for x in range(1,terrain_size[0]-1):
        for y in range(1,terrain_size[1]-1):
            if states[t-1,x,y] == 2: # it's on fire
                states[t,x,y] = 0 # put it out and clear it

                # if there's fuel surrounding it: set it on fire
                if states[t-1,x+1,y] == 1:
                    states[t,x+1,y] = 2
                if states[t-1,x-1,y] == 1:
                    states[t,x-1,y] = 2
                if states[t-1,x,y+1] == 1:
                    states[t,x,y+1] = 2
                if states[t-1,x,y-1] == 1:
                    states[t,x,y-1] = 2

colored = np.zeros((total_time,*terrain_size,3),dtype=np.uint8)

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

imageio.mimsave('./video.gif', cropped)
import numpy as np
import imageio
import copy
import grid

n = grid.n
total_time = n
states = [grid.grid[:] for t in range(n) ]

terrain_size = [grid.min_width, grid.min_height]

stateHolder = []

colored = np.zeros((total_time,*terrain_size,3),dtype=np.uint8)

# uma vez para cada elemento
for t in range(1,total_time):
    
    # pega versão anterior para usar como parâmetro
    states[t] = copy.copy(states[t-1]) # copia sem referenciar
    print('states[{}]={}'.format(t,states[t]))
    stateHolder.append(states[t])
    print(stateHolder[t-1])
    
    for i in range(n-1): # percorre linhas
        for j in range(n-1): # percorre colunas
            
            # fogo
            if states[t-1][i][j] == 100:
                print('fogo em [{}][{}][{}]'.format(t-1,i,j))
                states[t][i][j] = 0

                if states[t-1][i+1][j] == 1:
                    states[t][i+1][j] = 100
                    #print('passei 1')
                    #print('states[{}][{}][{}] agora é {}'.format(t,i+1,j,states[t][i+1][j]))
                if states[t-1][i-1][j] == 1:
                    states[t][i-1][j] = 100
                    #print('passei 2')
                    #print('states[{}][{}][{}] agora é {}'.format(t,i-1,j,states[t][i-1][j]))
                if states[t-1][i][j+1] == 1:
                    states[t][i][j+1] = 100
                    #print('passei 3')
                    #print('states[{}][{}][{}] agora é {}'.format(t,i,j+1,states[t][i][j+1]))
                if states[t-1][i][j-1] == 1:
                    states[t][i][j-1] = 100
                    #print('passei 4')
                    #print('states[{}][{}][{}] agora é {}'.format(t,i,j-1,states[t][i][j+1]))

            
            # área protegida
            if states[t-1][i][j] == 'x':
                print('área protegida em [{}][{}][{}] agora é {}'.format(t-1,i,j,states[t][i][j+1]))




#for t in range(len(stateHolder)):
 #   print(stateHolder[t])















colored = np.zeros((total_time,*terrain_size,3),dtype=np.uint8)

# Color
for t in range(len(stateHolder)): # linhas de states
    for x in range(n): # linhas de states[t]
        for y in range(n): # colunas de states[t]
            value = stateHolder[t].copy()

            if value[x][y] == 0:
                colored[t][x][y] = [139,69,19] # clear
            elif value[x][y] == 1:
                colored[t][x][y] = [0,255,0] # fuel
            elif value[x][y] == 100:
                colored[t][x][y] = [255,0,0] # burning

# Crop
cropped = colored[:200, 1:terrain_size[0]-1,1:terrain_size[1]-1]
imageio.mimsave('./video.gif', cropped)



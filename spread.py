import numpy as np
import imageio
import grid

found_protected = False

u = True if grid.win_dir == 'up' else False # up
d = True if grid.win_dir == 'down' else False # down
l = True if grid.win_dir == 'left' else False # right
r = True if grid.win_dir == 'right' else False # left

if grid.win_dir == 'reset':
    u,d,l,r == True # sem vento: todas as direções iguais


for t in range(1,grid.total_time):
    if not(found_protected):
        grid.states[t] = grid.states[t-1].copy()

        for i in range(1,grid.terrain_size[0]-1):
            for j in range(1,grid.terrain_size[1]-1):
                if grid.states[t-1,i,j] == 100: # it's on fire
                    grid.states[t,i,j] = -1 # put it out and clear it

                    # propaga o fogo imediatamente em vegetação rasteira
                    if (grid.states[t-1,i+1,j] == 1) and not(u):
                        grid.states[t,i+1,j] = 100
                    if (grid.states[t-1,i-1,j] == 1) and not(d):
                        grid.states[t,i-1,j] = 100
                    if (grid.states[t-1,i,j+1] == 1) and not(l):
                        grid.states[t,i,j+1] = 100
                    if (grid.states[t-1,i,j-1] == 1) and not(r):
                        grid.states[t,i,j-1] = 100
                    
                    # florestas demoram mais para queimar
                    if (grid.states[t-1,i+1,j] == 10) and not(u):
                        grid.states[t,i+1,j] = grid.states[t-1,i+1,j]/10
                    if (grid.states[t-1,i-1,j] == 10) and not(d):
                        grid.states[t,i-1,j] = grid.states[t-1,i-1,j]/10
                    if (grid.states[t-1,i,j+1] == 10) and not(l):
                        grid.states[t,i,j+1] = grid.states[t-1,i,j+1]/10
                    if (grid.states[t-1,i,j-1] == 10) and not(r):
                        grid.states[t,i,j-1] = grid.states[t-1,i,j-1]/10
                    
                    # não é combustível: aceiro/terra e água
                    # permanece com mesmo valor: não queima
                    if (grid.states[t-1,i+1,j] <= 0) and not(u):
                        grid.states[t,i+1,j] = grid.states[t-1,i+1,j]
                    if (grid.states[t-1,i-1,j] <= 0) and not(d):
                        grid.states[t,i-1,j] = grid.states[t-1,i-1,j]
                    if (grid.states[t-1,i,j+1] <= 0) and not(l):
                        grid.states[t,i,j+1] = grid.states[t-1,i,j+1]
                    if (grid.states[t-1,i,j-1] <= 0) and not(r):
                        grid.states[t,i,j-1] = grid.states[t-1,i,j-1]
                    
                    # área protegida: meta é evitá-la
                    # se chegar nela, a simulação finaliza
                    if (grid.states[t-1,i+1,j] == 2651) and not(u):
                        grid.states[t,i+1,j] = 100
                        found_protected = True
                    if (grid.states[t-1,i-1,j] == 2651) and not(d):
                        grid.states[t,i-1,j] = 100
                        found_protected = True
                    if (grid.states[t-1,i,j+1] == 2651) and not(l):
                        grid.states[t,i,j+1] = 100
                        found_protected = True
                    if (grid.states[t-1,i,j-1] == 2651) and not(r):
                        grid.states[t,i,j-1] = 100
                        found_protected = True
                    
                
                if grid.states[t-1,i,j] == -2: # água -> permanece
                    grid.states[t,i,j] = -2
                    
                if grid.states[t-1,i,j] == 0: # terra/aceiro -> permanece
                    grid.states[t,i,j] = 0
                


colored = np.zeros((grid.total_time,*grid.terrain_size,3),dtype=np.uint8)git 

# Color
for t in range(grid.states.shape[0]):
    for i in range(grid.states[t].shape[0]):
        for j in range(grid.states[t].shape[1]):
            value = grid.states[t,i,j].copy()

            if value == -2:
                colored[t,i,j] = grid.blue # água
            elif value == -1:
                colored[t,i,j] = grid.black # queimada
            elif value == 0:
                colored[t,i,j] = grid.brown # terra/aceiro
            elif value == 1:
                colored[t,i,j] = grid.green # vegetação rasteira
            elif value == 10:
                colored[t,i,j] = grid.forest # vegetação
            elif value == 100:
                colored[t,i,j] = grid.red # fogo
            elif value == 2651:
                colored[t,i,j] = grid.gold # área protegida

# Crop
cropped = colored[:200, 1:grid.terrain_size[0]-1,1:grid.terrain_size[1]-1]

imageio.mimsave('./video.gif', cropped)
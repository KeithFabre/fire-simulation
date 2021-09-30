import numpy as np 
import imageio # para exportar como gif

# 0 = Clear, 1 = Combustível, 2 = Fogo

prob = .6 # prob. de uma célula ser combustível, ou é clear
total_time = 300 # tempo de simulação
terrain_size = [100, 100] # tamanho da simulação

states = np.zeros((total_time, *terrain_size))
states[0] = np.random.choice([0,1], size=terrain_size,p=[1-prob, prob])
# célula do meio pegando fogo
states[0,terrain_size[0]//2,terrain_size[1]//2]=2

for t in range(1, total_time):
    # copia os estados originais
    states[t] = states[t-1].copy()

    for x in range(1, terrain_size[0]-1):
        for y in range(1, terrain_size[1]-1):

            if states[t-1,x,y] == 2: # está pegando fogo
                states[t,x,y] = 0 # apaga e limpa

                # se tem compustível ao redor
                # incendeia!
                if states[t-1,x+1,y] == 1:
                    states[t,x+1,y] = 2
                if states[t-1,x-1,y] == 1:
                    states[t,x-1,y] = 2
                if states[t-1,x,y+1] == 1:
                    states[t,x,y-1] = 2

colored = np.zeros((total_time,*terrain_size,3),dtype=np.uint8)

# Cor
for t in range(states.shape[0]):
    for x in range(states[t].shape[0]):
        for y in range(states[t].shape[1]):
            value = states[t,x,y].copy()

            if value == 0:
                colored[t,x,y] = [139,69,19] # clear
            elif value == 1:
                colored[t,x,y] = [0,255,0] # combustível
            elif value == 2:
                colored[t,x,y] = [255,0,0] # queimando

# Corte
cropped = colored[:200, 1:terrain_size[0]-1,1:terrain_size[1]-1]

imageio.mimsave('./simulacao.gif', cropped)


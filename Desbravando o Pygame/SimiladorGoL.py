import random
import time
import pygame
import jogo as jg

def desenha_matriz(matriz):
    """
    Função para desenhar o plano    
    """
    #prenche a tela de preto
    screen.fill([0, 0, 0])

    #percorre o plano desenhando as células com seus valors
    for r, linha in enumerate(matriz):
        for c, célula in enumerate(linha):
            if célula:
                #caso a célula esteja viva, a pinte de branco.
                pygame.draw.rect(screen, (255, 255, 255),(11*c, 11*r, 10, 10))

# plano vazio
SEED = [[0 for _ in range(50)] for _ in range(50)]

#Glider
#SEED[23][24] = 1
#SEED[24][25] = 1
#SEED[25][23] = SEED[25][24] = SEED[25][25] = 1

#Randon
#SEED = [[random.choice([0, 1])for _ in range(50)] for _ in range (50)]
pygame.init()

screen = pygame.display.set_mode((550, 550))

#define seed como um dos valores de exemplo do começo
seed = SEED

#desenha o estado inicial da nossa seed.
desenha_matriz(seed)

pygame.display.flip()

time.sleep(1)

while True:
    #processamento de entrada
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        #finaliza o programa caso clique em fechar
        break
    elif (event.type == pygame.KEYDOWN and event.key == event.K_ESCAPE):
        #finaliza o programa caso pressione ESC
        break

    seed = jg.jogo_da_vida(seed)

    #Desenho

    #desenha nova geração na tela
    desenha_matriz(seed)

    pygame.display.flip()

    time.sleep(0.05)
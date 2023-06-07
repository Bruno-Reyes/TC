import numpy as np
import pygame
import time

# Funciones ------------------------------

# Creamos el tablero
def create_board(nxC, nyC):
    board = []
    value = 1
    for x in range(nxC):
        row = []
        for x in range(nyC):
            row.append(value)
            value = 0 if value == 1 else 1
        board.append(row)

    board[1] = board[1][::-1]
    board[3] = board[3][::-1]
    return np.array(board)

# Animacion
def play(board, nxC, nyC):

    # Tamaño de la ventana (pixeles)
    width, height = 600, 600
    # Dimensiones de la celda
    dimCW = width / nxC
    dimCH = height / nyC
    # Inicializamos pygame
    pygame.init()
    # Definimos la ventana
    screen = pygame.display.set_mode((height, width))
    # Comienza el juego
    while True:

        # Agregamos delay 
        time.sleep(0.1)

        # Calculo de tamaño de los poligonos (celda)
        for y in range(0, nxC):
            for x in range(0, nyC):
                # Creamos el poligono de cada celda a dibujar
                poly = [((x) * dimCW, y * dimCH),
                        ((x+1) * dimCW, y * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ((x) * dimCW, (y+1) * dimCH)]

                # Y dibujamos la celda para cada par de celdas de x e y
                if board[x,y] == 0:
                    pygame.draw.polygon(screen, (94, 14, 153), poly, 0) # Azul
                else: 
                    pygame.draw.polygon(screen, (15, 195, 190), poly, 0) # Morado

        # Actualizamos la ventana
        pygame.display.flip()

# ------------------------------------------------ #

# Ejecucion principal
# Numero de celdas
nxC, nyC = 4, 4
#---- #play(board, nxC, nyC)
# Instanciamos el tablero
board = create_board(nxC, nyC)

sequency = input('Introduce la secuencia de juego :P (amam)--> ')
print(sequency)



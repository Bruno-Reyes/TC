# Importamos librerias 
import numpy as np 
from time import sleep
import networkx as nx
import matplotlib.pyplot as plt
    
# Creamos el automata
class ADF:
    def __init__(self, cadena:list):
        self.cadena = cadena
        self.estado = 0 

    def imparidad(self):
        for c in self.cadena:
            self.funcion_transicion(c)

        if self.estado == 0:
            return False
        else: 
            return True
            
    def funcion_transicion(self, caracter):
        # Estado Q0
        if self.estado == 0: 
            if caracter == 0:
                self.estado = 2
            else: 
                self.estado = 1

        # Estado Q1     
        elif self.estado == 1: 
            if caracter == 0:
                self.estado = 3
            else: 
                self.estado = 0

        # Estado Q2 
        elif self.estado == 2: 
            if caracter == 0:
                self.estado = 0
            else: 
                self.estado = 3

        # Estado Q3     
        elif self.estado == 3: 
            if caracter == 0:
                self.estado = 1
            else: 
                self.estado = 2

    def cadena_str(self):
        binaria = ''
        for c in self.cadena:
            binaria += str(c)
        return binaria


def ejecutarProtocolo(generadas, aceptadas, rechazadas):
    # Generar 10^6 cadenas binarias aleatoriamente de longitud 64.
    no_cadenas = 1000000
    long_cadenas = 64
    cadenas =  np.random.randint(2, size=(no_cadenas, long_cadenas))

    # Hacer que el programa espere 3 segundos. 
    print('Iniciando protocolo. . .')
    sleep(3)
    print('Ejecutando protocolo. . .')

    for i in range(cadenas.shape[0]):
        
        automata = ADF(cadenas[i,:])
        cadena = automata.cadena_str()
        # Agregamos al archivo de las cadenas generadas
        generadas.write(cadena+'\n')

        # Agregamos cadena al archivo correspondiente
        if automata.imparidad(): 
            aceptadas.write(cadena+'\n')
        else: 
            rechazadas.write(cadena+'\n')
 

corrida = 1
encendido = True

#Abrimos los archivos.
generadas = open('CadenasGeneradas.txt', mode='w')
aceptadas = open('CadenasAceptadas.txt', mode='w')
rechazadas = open('CadenasRechazadas.txt', mode='w')

while encendido:
    generadas.write('EJECUCION '+str(corrida)+'\n')
    aceptadas.write('EJECUCION '+str(corrida)+'\n')
    rechazadas.write('EJECUCION '+str(corrida)+'\n')

    ejecutarProtocolo(generadas, aceptadas, rechazadas)
    corrida+= 1
    encendido = False if np.random.randint(2) == 0 else True

print('Ejecución de protocolos terminada. . .')
# Cerramos los archivos.
generadas.close()
aceptadas.close()
rechazadas.close()

# Graficando representacion visual de automata

# Agregar arista
def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)

G = nx.Graph()

# Agregar nodos y aristas
agregar_arista(G, "Ready", "End", "No")
agregar_arista(G, "Ready", "Generate", "Yes")
agregar_arista(G, "Generate", "q0", "Timeout")
agregar_arista(G, "q0", "q2", 0)
agregar_arista(G, "q2", "q0", 0)
agregar_arista(G, "q0", "q1", 1)
agregar_arista(G, "q1", "q0", 1)
agregar_arista(G, "q1", "q3", 0)
agregar_arista(G, "q3", "q1", 0)
agregar_arista(G, "q2", "q3", 1)
agregar_arista(G, "q3", "q2", 1)
agregar_arista(G, "q0", "Append", "pair")
agregar_arista(G, "q1", "Append", "odd")
agregar_arista(G, "q2", "Append", "odd")
agregar_arista(G, "q3", "Append", "odd")
agregar_arista(G, "Append", "Ready", False)

# Draw the networks
pos = nx.layout.planar_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Protocolo")
plt.show()
import random # Libreria 'random'
import os # Libreria para manejo de archivos

print('Automata de pila!')  

print('Deseas que el lenguaje se genere de forma manual o automática?') # Modo de creacion de la cadena
modo = int(input((" 0. Manual\n 1.Automatica\n")))
cadena = ''
if modo == 0: # Manual: Pedimos al usuario que introduzca la cadena
    cadena = str(input('Cadena binaria --> '))
else: # Automático: Creamos la cadena con 0's y 1's (50% probabilidad por elemento)
    n = random.randint(0,100000)
    cadena += '0'
    for i in range(n-1):
        cadena += str(random.randint(0,1))

# Definimos estructura "Pila
class Pila: 
    def __init__(self):
        self.items = ['X'] # Instanciamos la pila con una 'X' en el fondo
    
    def agregar(self, item): # Agregamos un elemento a la pila 
        self.items.append(item)
    
    def extraer(self):  # Extraemos el ultimo elemento de la pila
        self.items.pop()

    def inspeccionar(self): # Consultamos el tope de la pila
        return self.items[len(self.items)-1]

    def imprimir(self): # Imprimimos la pila completa
        contenido = ''
        for item in self.items[::-1]:
            contenido += item
        return contenido

# Definimos el automata de pila
class PDA: 
    def __init__(self, cadena):
        self.cadena = cadena # Cadena que se va a evaluar
        self.q0 = True # Estado q0
        self.q1 = False # Estado q1
        self.q2 = False # Estado q2
        self.q3 = False # Estado q3
        self.stack = Pila() # Instanciamos una pila

    def escribirArchivo(self,historial): 
        with open('./Automata de pila/Historial.txt', mode='w', encoding='utf-8') as archivo: 
            archivo.write(historial)
        archivo.close()

    def evaluar(self): # Control de estados finitos
        historial = '(q0 , '+cadena+' , '+str(self.stack.imprimir())+')\n'
        for i in range(len(self.cadena)): # Recorremos la cadena  
            if self.q0: # Cuando estado q0 esta activo
                historial += '(q0 , '
                if self.cadena[i] == '0':
                    self.stack.agregar('a')
                elif self.cadena[i] == '1' and self.stack.inspeccionar()=='a':
                    self.stack.extraer()
                    self.q0 = False
                    self.q1 = True
            elif self.q1: # Cuando estado q1 esta activo
                historial += '(q1 , '
                if self.cadena[i] == '1' and self.stack.inspeccionar()=='a':
                    self.stack.extraer()
                elif self.cadena[i] == '1' and self.stack.inspeccionar()=='X':
                    self.stack.agregar('a')
                    self.q1 = False
                    self.q2 = True
            elif self.q2: # Cuando estado q2 esta activo
                historial += '(q2 , '
                if self.cadena[i] == '1':
                    self.stack.agregar('a')
            historial += str(self.cadena[i+1::])+' , '+str(self.stack.imprimir())+')'+'\n'
        if self.stack.inspeccionar() == 'X': # Cuando termina la cadena verificamos el tope de la pila
            self.q1 = False
            self.q2 = False
            self.q3 = True # Si el tope de la pila es 'X', la vaciamos y aceptamos la cadena
            historial += '(q3 , e , )\n'
        if self.q3:
            historial += '¡Cadena Aceptada!'
        else: 
            historial += '¡Cadena Rechazada!'
        self.escribirArchivo(historial)
        return self.q3

print(cadena) # Mostramos la cadena a evaluar
automata = PDA(cadena)  # Instanciamos el autómata con la cadena a evaluar
print(automata.evaluar()) # Usamos el método evaluar para saber si la cadena es valida ó no 
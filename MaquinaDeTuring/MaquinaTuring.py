import random # Libreria para numeros aleatorios
print('Maquina de Turing!')

# Preguntamos si queremos que la construccion sea automatica o manual
print('¡Deseas ingresar la cadena o que se genere automaticamente?')
modo = int(input((" 0. Manual\n 1.Automatica\n")))
cadena = ''
if modo == 0:
    cadena = input('¿Cual es la cadena? (*|n*|m*)--> ') # Solicitamos la cadena
else: 
    # Generamos la cadena usando 'n' y 'm' de forma aleatoria
    n = random.randint(1,45)
    m = random.randint(1,46-n)
    cadena = '*'+'|'*n+'*'+'|'*m+'*'

print('La cadena es --> \'{}\''.format(cadena))

#cadena = '*|*||*'

# Definimos la maquina de Turing usando una clase
class maquinaTuring():
    # Metodo constructor
    def __init__(self,cadena):
        self.cadena = [c for c in cadena] # Recibe la cadena y la convierte en una lista de numeros
        self.estado = '1' # El estado inicial es 1
        self.salida = '' # Salida del programa será una cadena
        self.historial = '' # Historial: Almacena los cambios realizados en cada ciclo de la maquina
    
    def funcion_transicion(self, caracter): # Retornara el valor a sustituir y direccion el estado se cambia desde la funcion 
        if self.estado == '1':
            if caracter == '*':
                self.estado = '2'
                return ('X', 1)
        if self.estado == '2':
            if caracter == '*':
                self.estado = '3'
                return ('*', 1)
            if caracter == '|':
                self.estado = '2'
                return ('|', 1)
        if self.estado == '3':
            if caracter == '*':
                self.estado = '4'
                return ('X', -1)
            if caracter == '|':
                self.estado = '3'
                return ('|', 1)
        if self.estado == '4':
            if caracter == '*':
                self.estado = '4'
                return ('*', -1)
            if caracter == '|':
                self.estado = '5'
                return ('a', 1)
            if caracter == 'X':
                self.estado = '7'
                return ('X', 1)
        if self.estado == '5':
            if caracter == ' ':
                self.estado = '6'
                return ('|', -1)
            if caracter == '*':
                self.estado = '5'
                return ('*', 1)
            if caracter == '|':
                self.estado = '5'
                return ('|', 1)
            if caracter == 'X':
                self.estado = '5'
                return ('X', 1)
        if self.estado == '6':
            if caracter == '*':
                self.estado = '6'
                return ('*', -1)
            if caracter == '|':
                self.estado = '6'
                return ('|', -1)
            if caracter == 'a':
                self.estado = '4'
                return ('|', -1)
            if caracter == 'X':
                self.estado = '6'
                return ('X', -1)
        if self.estado == '7':
            if caracter == '*':
                self.estado = '8'
                return ('*', 1)
            if caracter == '|':
                self.estado = '7'
                return ('|', 1)
        if self.estado == '8':
            if caracter == ' ':
                self.estado = '9'
                return ('*', -1)
            if caracter == '|':
                self.estado = '8'
                return ('|', 1)
            if caracter == 'X':
                self.estado = '8'
                return ('*', 1)
        if self.estado == '9':
            if caracter == '*':
                self.estado = '9'
                return ('*', -1)    
            if caracter == '|':
                self.estado = '9'
                return ('|', -1)
            if caracter == 'X':
                self.estado = '0'
                return ('*', 0)
    
    # Para evitar desbordamientos en la lista, en cada ciclo agregamos un espacio vacio al final
    # de la lista, solo si no existe
    def reajuste(self):
        if self.cadena[-1] != ' ':
            self.cadena.append(' ')

    # Metodo para convertir la lista de valores (cinta) en una cadena de texto
    def convertir(self):
        cadena = ''
        for i in self.cadena:
            cadena += i
        return cadena    
    
    # Metodo para guardar el cambio por cada ciclo de la maquina
    # Si recibe true, guarda el historial en un archivo
    def escribirArchivo(self, guardarArchivo = False):
        if guardarArchivo:
            self.historial += '(q{}, {} )'.format(self.estado, self.convertir())
            archivo = open('./MaquinaDeTuring/HistorialTuring.txt', mode='w', encoding='utf-8')
            archivo.write(self.historial)
            archivo.close()
        else:
            self.historial += '(q{}, {})\n'.format(self.estado, self.convertir())

    # Endendemos la maquina de Turing que usa los metodos anteriores para funcionar
    def evaluar(self):
        # La cabecilla del lector comienza por el extremo izquierdo de la lista
        lector = 0
        # El criterio de paro es el estado 0
        while self.estado != '0':
            self.escribirArchivo() # Guardamos estado actual de la maquina
            valor, direccion  = self.funcion_transicion(self.cadena[lector]) # Leemos valor en la lista y usamos la funcion de transicion
            self.cadena[lector] = valor # Reemplazamos el valor indicado por las reglas definidas en la posicion del lector
            lector += direccion # Movemos la cabezilla del lector en la direccion indicada
            self.reajuste() # Reajustamos la cadena si es necesario

        self.escribirArchivo(guardarArchivo=True) # Cuando la maquina termina, guardamos su estado por ultima vez y escribimos archivo en disco duro
        self.salida = self.convertir() # Establecemos la salida como cadena de texto
    

# Creamos un objeto de nuestra clase definida, dandole la cadena a evaluar
maquina = maquinaTuring(cadena) 

# Encendemos la maquina
maquina.evaluar()

# Consultamos salida de la maquina
print('Salida de la maquina de Turing --> '+maquina.salida)
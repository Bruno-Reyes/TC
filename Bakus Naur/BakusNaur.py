# Importamos librerias
import random 
import re

print('Bakus Naur!')
# Preguntamos si queremos que la construccion sea automatica o manual
print('Deseas que el numero de derivaciones se eliga de forma manual o automatica?')
modo = int(input((" 0. Manual\n 1.Automatica\n")))
n = ''
if modo == 0:
        n = int(input('Numero de derivaciones? --> ')) # Solicitamos el numero de derivaciones
else: 
    n = random.randint(1,100) # Generamos la longitud de forma aleatoria

# Funcion que devuelve una regla de produccion en funcion a un caracter recibido
def reglas_produccion(caracter:str): 
    gramatica = {"S" : "iCtSA",
                 "A" : ";eS",
                }
    return gramatica[caracter]

# Funcion que realiza las derivaciones segun un numero dado
def derivaciones(n): 
    # Usamos una variable historial para almacenar los cambios
    historial = 'Numero de derivaciones por hacer --> {}\n'.format(n) 
    cadena = 'S' # Definimos la cadena a derivar
    historial += cadena+'\n' # Agregamos al historial
    # Iteramos n veces con n = derivaciones deseadas
    for i in range(n): 
        cadena = cadena.replace('S', reglas_produccion('S')) # En cada iteracion reemplazamos 'S' por la regla de produccion 'S'
        historial += cadena+'\n' # Agregamos el cambio al historial

    cadena = cadena.replace('A', reglas_produccion('A')) # Cuando terminan las iteraciones reemplazamos 'A' por la regla 'A'
    historial += cadena # Agregamos el cambio al historial

    # Creamos un archivo para guardar el historial
    archivo = open('./Construccion.txt', mode='w',encoding='utf-8')
    archivo.write(historial) # Guardamos el historial
    archivo.close() # Cerramos el archivo
    return cadena # Regresamos la cadena creada

print(derivaciones(n)) # Invocamos la funcion derivaciones

# PARA LA CREACION DE PSEUDO-CODIGO
# Abrimos el archivo construido en modo lectura
file = open('./Construccion.txt', mode='r', encoding='utf-8')
lines = file.read() # Leemos el archivo 
file.close() # Cerramos el archivo
instrucciones = lines.split('\n')[-1] # Tomamos la ultima linea 
instrucciones = instrucciones.split(';') # Separamos la cadena a una lista usando ';' como separacion
aperturas = re.findall('iCt', instrucciones[0]) # Buscamos todas las estructuras if
instrucciones.pop(0) # Quitamos las estructuras if

estructura = '' # Usaremos una variable estructura donde almacenaremos el pseudo-codigo
tabulaciones = 0 # Comenzamos con 0 tabulaciones
for a in aperturas: # Iteramos en las aperturas de if 
    estructura += '\t'*tabulaciones+'if conditional {\n' # Escribimos las tabulaciones con el if
    tabulaciones += 1 # Sumamos en 1 las tabulaciones
estructura += '\t'*tabulaciones+'sentence\n' # Agregamos la sentencia final del if

for e in instrucciones:# Agregamos las cerraduras iterando en ellas
    tabulaciones -= 1  # Comenzamos disminuyendo en 1 las tabulaciones
    estructura += '\t'*tabulaciones+'else {\n' # Escribimos las tabulaciones con el else
    estructura += '\t'*(tabulaciones+1)+'sentence\n'  # Agregamos la sentencia final del else con una tabulacion adicional

pseudo = open('./Pseudo-codigo.txt', mode='w', encoding='utf-8') # Abrimos el archivo pseudo-codigo
pseudo.write(estructura) # Escribimos la estructura que acabamos de construir
pseudo.close() # Cerramos el archivo 



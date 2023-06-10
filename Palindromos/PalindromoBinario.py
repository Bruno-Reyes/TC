import random

print('Programa Palindromos!')

# Preguntamos si queremos que la construccion sea automatica o manual
print('¡Deseas que la longitud del palindromo eliga de forma manual o automatica?')
modo = int(input((" 0. Manual\n 1.Automatica\n")))
longitud = ''
if modo == 0:
        longitud = int(input('¿Longitud del palindromo? --> ')) # Solicitamos la longitud del palindromo
else: 
    longitud = random.randint(1,100000) # Generamos la longitud de forma aleatoria

print('La longitud del palindromo será de {}'.format(longitud))

# Funcion que devuelve una regla de produccion de forma aleatoria en funcion del numero de terminales que posee
def regla_produccion(nivel:str): 
    gramatica = {"0" : [[""]],
                 "1" : [["0"], ["1"]],
                 "2" : [["0", "P", "0"], ["1", "P", "1"]]
                 }
    return "".join(random.choice(gramatica[nivel]))

# Funcion para generar palindromo
def generar_palindromo(longitud:int):
    #Guardaremos la construccion del palindromo en una cadena para despues escribir en un archivo
    construccion = "Longitud del palindromo a construir --> "+str(longitud)+"\n" 
    archivo = open('./Palindromos/Construccion.txt', mode='w', encoding='utf-8') # Creamos y/o abrimos el archivo 
    palindromo = "P" # Definimos nuestro palindromo inicial como P
    construccion += palindromo+"\n" 
    while longitud > 1: # Si la longitud del palindromo es mayor a 1
        produccion = regla_produccion("2") # Solicitamos una regla de produccion con 2 terminales
        palindromo = palindromo.replace("P", produccion) # Reemplazamos la variable P por regla de produccion obtenida
        construccion += "Regla de produccion --> "+str(produccion)+"\n" # Informamos que regla de produccion se usó
        construccion += palindromo+"\n" # Agregamos la cadena resultante a nuestra construccion
        longitud -= 2 # Restamos a la longitud 2 (numero de terminales agregadas)

    if longitud == 1: # Si la longitud es 1 
        produccion = regla_produccion("1") # Solicitamos una regla de produccion con 1 terminales
        palindromo = palindromo.replace("P", produccion) # Reemplazamos la variable P por regla de produccion obtenida
        construccion += "Regla de produccion --> "+str(produccion)+"\n" # Informamos que regla de produccion se usó
        construccion += palindromo # Agregamos la cadena resultante a nuestra construccion

    else:
        produccion = regla_produccion("0") # Solicitamos una regla de produccion con 0 terminales
        palindromo = palindromo.replace("P", produccion) # Reemplazamos la variable P por regla de produccion obtenida
        construccion += "Regla de produccion --> e\n" # Informamos que regla de produccion se usó
        construccion += palindromo # Agregamos la cadena resultante a nuestra construccion
    archivo.write(construccion) # Escribimos toda la construccion en el archivo
    archivo.close() # Cerramos el archivo
    return palindromo # Retornamos el palindromo generado 
    
generar_palindromo(longitud)
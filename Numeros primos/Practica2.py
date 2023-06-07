import numpy as np 
import time
print('¡Practica 2!')

# Establecimiento de parámetros

# Tipo de universo
print('El universo se creará de forma: ')
print('0. Automática')
print('1. Manual')

modo = int(input('?. '))

# Asignación de n
n = -1

if modo == 0:
    n = np.randint(3, 10000001)
else: 
    while n == -1:
        n_temporal = int(input('¿Cuál será el valor de \'n\'? (Rango: 0-10,000,000): '))
        if n_temporal >= 0 and n_temporal <= 10000000:
            n = n_temporal

print('El valor de \'n\' es: '+str(n))

# Creacion de la lista de números

universo = np.array(list(range(2, n+1)))
# Criba de Eratostenes

primo = 2 
bandera = True
tiempos = {'Inicio': str(time.strftime("%H:%M:%S"))}
with open('./Primos.txt', mode='w') as archivo:
    archivo.write('{ \n')
    while bandera:
        universo = np.delete(universo, 0)
        universo_temporal = np.copy(universo)
        archivo.write(str(primo)+', \n')
        #print('Eliminando multiplos de '+str(primo))
        for i in range(universo.shape[0]):
            if universo[i]%primo == 0:
                universo_temporal = np.delete(universo_temporal, np.where(universo_temporal==universo[i]))
        universo = np.copy(universo_temporal)
        
        if universo.shape[0] == 0:
            bandera = False
        else: 
            primo = universo[0]
    archivo.write('}')
archivo.close()

tiempos['Fin'] = str(time.strftime("%H:%M:%S"))

print(tiempos)
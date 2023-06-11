import pygame
import threading

def animacion():
    # Dimensiones de la ventana
    tamano = (800, 1000)

    # Dimensiones del rectángulo 
    rectangulo = (int(tamano[0]/5), int((tamano[1]/10)*8))

    # Abrimos archivo y preparamos los datos
    datos = []
    archivo = open('./Automata de pila/Historial.txt', mode='r', encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()
    tamano_pila = 0
    for linea in lineas[:-1]: 
        dato = linea.replace('\n','').replace('(','').replace(')','').replace(' ','').split(',')
        if len(dato[2]) >tamano_pila:
            tamano_pila = len(dato[2])
        datos.append(dato)
    resultado = lineas[-1]
    # Inicializar Pygame
    pygame.init()

    # Crear la ventana
    pantalla = pygame.display.set_mode(tamano)
    pygame.display.set_caption("Automata de pila")

    # Colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    VERDE =(78,205,74)

    # Crear un objeto de fuente
    fuente = pygame.font.Font(None, 36)
    fuente_cadena = pygame.freetype.Font(None, 36)
    # Ciclo principal del juego
    ejecucion = True
    while ejecucion:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecucion = False

        # Limpiar la ventana
        pantalla.fill(BLANCO)
        
        for iteracion in datos:
            # Limpiar el texto
            pantalla.fill(BLANCO)
            estado_iteracion = iteracion[0]
            cadena_iteracion = iteracion[1]
            pila_iteracion = iteracion[2]

            # Crear una superficie de texto
            texto_superficie_resultado, texto_rectangulo_resultado = fuente_cadena.render(resultado, NEGRO)
            # Centrar el texto en la coordenada
            texto_rectangulo_resultado.center = (tamano[0]//2, tamano[1]//20)
            # Dibujar el texto en la ventana
            pantalla.blit(texto_superficie_resultado, texto_rectangulo_resultado)
            # Dibujar el rectángulo
            pygame.draw.rect(pantalla, NEGRO, ((tamano[0]/5)*3,(tamano[0]/10), rectangulo[0], rectangulo[1]), 3)
            
            # Dibujar las cajas para los estados
            ancho_division = rectangulo[1] // 4
            for i in range(1, 4):
                y = (ancho_division * i) + tamano[1]//10
                pygame.draw.line(pantalla, NEGRO, ((tamano[0]/5)*3, y), ((tamano[0]/5)*4, y), width=3)
            
            # Escribir el estado dentro de cada caja
            x = tamano[0] // 5
            estado = 0
            for j in range(1,8,2):
                estado_texto = 'q'+str(estado)
                if estado_texto == estado_iteracion:
                    pygame.draw.circle(pantalla,VERDE, (x*3+x/2, tamano[1]//10 + (rectangulo[1]//4//2)*j), radius= 40 )
                
                texto = fuente.render(estado_texto, True, NEGRO)
                pantalla.blit(texto, (x*3+x/2 - 12,tamano[1]//10 + (rectangulo[1]//4//2)*j - 15))
                estado += 1

            
            x_abs_texto = tamano[0] // 5
            x_abs_texto += x_abs_texto//2

            y_abs_texto = tamano[1] // 10 * 9
            alto_division = rectangulo[1]// tamano_pila // 2
            k = 1
            for c in pila_iteracion[::-1]:
                # Crear una superficie de texto
                texto_superficie, texto_rectangulo = fuente_cadena.render(c, NEGRO)
                # Centrar el texto en la coordenada
                texto_rectangulo.center = (x_abs_texto, y_abs_texto - alto_division*(k+1) + alto_division//2)
                # Dibujar el texto en la ventana
                pantalla.blit(texto_superficie, texto_rectangulo)
                k += 1

            # Crear una superficie de texto
            texto_superficie, texto_rectangulo = fuente_cadena.render(cadena_iteracion, NEGRO)
            # Centrar el texto en la coordenada
            texto_rectangulo.center = (tamano[0]//2, (tamano[1]//20) * 19)
            # Dibujar el texto en la ventana
            pantalla.blit(texto_superficie, texto_rectangulo)
            # Actualizar la ventana
            pygame.display.flip()

            # Esperar un momento para que se muestre el texto    
            if estado_iteracion == 'q3':
                pygame.time.wait(3000)
            else:
                pygame.time.wait(400)
            
    # Salir del programa
    pygame.quit() 
    

if __name__ == '__main__':
    # Crear un hilo para ejecutar la aplicación de Pygame
    pygame_thread = threading.Thread(target=animacion)
    pygame_thread.start()

    # Esperar hasta que el hilo de Pygame termine
    pygame_thread.join()
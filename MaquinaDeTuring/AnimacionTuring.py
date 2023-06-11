import pygame
import threading

def animacion():
    # Dimensiones de la ventana
    tamano = (1200, 800)

    # Dimensiones del rectángulo
    rectangulo = (int((tamano[0]/12)*10), int(tamano[1]/5))

    # Abrimos archivo y preparamos los datos
    datos = []
    archivo = open('./MaquinaDeTuring/HistorialTuring.txt', mode='r', encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas: 
        dato = linea.replace('\n','').replace('(','').replace(')','').replace(' ','')
        datos.append(dato.split(','))

    # Inicializar Pygame
    pygame.init()

    # Crear la ventana
    pantalla = pygame.display.set_mode(tamano)
    pygame.display.set_caption("Maquina de Turing")

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
            # Dibujar el rectángulo
            pygame.draw.rect(pantalla, NEGRO, (tamano[0]/12,(tamano[1]/5)*3, rectangulo[0], rectangulo[1]), 3)

            # Dibujar las cajas para los estados
            ancho_division = rectangulo[0] // 10
            for i in range(1, 10):
                x = (ancho_division * i) + tamano[0]/12
                pygame.draw.line(pantalla, NEGRO, (x, (tamano[1]/5)*3), (x, (tamano[1]/5)*4), width=3)

            # Escribir el estado dentro de cada caja
            x_texto_division = tamano[0] // 24
            estado = 0
            for j in range(2,21,2):
                estado_texto = 'q'+str(estado)
                if estado_texto == estado_iteracion:
                    pygame.draw.circle(pantalla,VERDE, (x_texto_division*j+x_texto_division, (tamano[1]/5)*3 + tamano[1]/10), radius= 30 )
                
                texto = fuente.render(estado_texto, True, NEGRO)
                pantalla.blit(texto, (x_texto_division*j+x_texto_division - 15, (tamano[1]/5)*3 + tamano[1]/10 -15))
                estado += 1
            
            # Crear una superficie de texto
            texto_superficie, texto_rectangulo = fuente_cadena.render(cadena_iteracion, NEGRO)
            # Centrar el texto en la ventana
            texto_rectangulo.center = (tamano[0] // 2, tamano[1]//5 * 1 + tamano[1]//10)

            # Dibujar el texto en la ventana
            pantalla.blit(texto_superficie, texto_rectangulo)
            
            # Actualizar la ventana
            pygame.display.flip()

            # Esperar un momento para que se muestre el texto    
            if estado_iteracion == 'q0':
                pygame.time.wait(3000)
            else:
                pygame.time.wait(10)
            
    # Salir del programa
    pygame.quit() 

if __name__ == '__main__':
    # Crear un hilo para ejecutar la aplicación de Pygame
    pygame_thread = threading.Thread(target=animacion)
    pygame_thread.start()

    # Esperar hasta que el hilo de Pygame termine
    pygame_thread.join()
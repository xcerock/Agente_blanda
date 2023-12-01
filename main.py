import pygame
import sys
import time
import random

class Agente:
    
    def __init__(self,volumen = int,temperatura = int):
        self.volumen = volumen
        self.temperatura = temperatura
        self.estado = 0
    #Se cambia el estado del entorno con base a las percepciones que recibe el agente
        if (volumen <= 90 and temperatura in range(20, 25)):
            estado = 1 #Adecuado
        if (volumen <= 90 and temperatura < 20):
            estado = 2 #Exceso de frio
        if (volumen <= 90 and temperatura > 25):
            estado = 3 #Exceso de calor
        if (volumen > 90 and temperatura in range(20, 25)):
            estado = 4 #Exceso de ruido
        if (volumen > 90 and temperatura < 20):
            estado = 5 #Exceso de ruido y temperatura baja
        if (volumen > 90 and temperatura > 25):
            estado = 6 #Exceso de ruido y temperatura alta

def main():
    # Inicializar Pygame
    pygame.init()

    # Definir dimensiones de la ventana
    width, height = 720, 720

    # Crear la ventana
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Discoteca")

    # Cargar la imagen de fondo
    discoteca_gente1 = pygame.image.load("discoteca_gente1.png")  
    discoteca_gente2 = pygame.image.load("discoteca_gente2.png")  
    discoteca_gente3 = pygame.image.load("discoteca_gente3.png")  
    discoteca_gente4 = pygame.image.load("discoteca_gente4.png")  
    discoteca = pygame.image.load("discoteca.png")  
    discoteca = pygame.transform.scale(discoteca, (width, height))
    

    # Configurar la fuente para el texto
    font = pygame.font.Font(None, 36)

    # Inicializar variables de tiempo
    hora = 5
    minuto = 0

    # Inicializar variables de temperatura y volumen
    current_temperature = 8
    current_volume = 0

    gente = 0

    # Bucle principal
    while True:
        minuto += 15
        if minuto == 60:
            minuto = 0
            hora += 1
            gente = random.randint(0, 400)
            if gente >= 300:
                current_temperature = random.randint(25, 30)
                current_volume = random.randint(80, 100)
            elif gente >= 200:
                current_temperature = random.randint(20, 25)
                current_volume = random.randint(60, 80)
            elif gente >= 100:
                current_temperature = random.randint(15, 20)
                current_volume = random.randint(40, 60)
            elif gente < 100:
                current_temperature = random.randint(10, 15)
                current_volume = random.randint(20, 40)    
            else:
                current_temperature = random.randint(15, 30)
        if hora == 24:
            hora = 0
        time.sleep(1)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if hora >= 20 or hora < 5:
            print(gente)
            if gente >= 300:
                background_image = pygame.transform.scale(discoteca_gente4, (width, height))
            elif gente >= 200:
                background_image = pygame.transform.scale(discoteca_gente3, (width, height))
            elif gente >= 100:

                background_image = pygame.transform.scale(discoteca_gente2, (width, height))
            elif gente < 100:

                background_image = pygame.transform.scale(discoteca_gente1, (width, height))
        else:
            current_volume = 0 
            background_image = pygame.transform.scale(discoteca, (width, height))
            

        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0)) 
        # Renderizar y mostrar el texto de la hora
        text_time = font.render("Hora: " + str(hora) + ":" + str(minuto) , True, (255, 255, 255))
        screen.blit(text_time, (10, 10))

        # Simular valores de temperatura y volumen (reemplaza con tus datos reales

        # Renderizar y mostrar el texto de la temperatura
        text_temperature = font.render("Temperatura: " + str(current_temperature) + "°C", True, (255, 255, 255))
        screen.blit(text_temperature, (10, 50))

        # Renderizar y mostrar el texto del volumen
        text_volume = font.render("Volumen: " + str(current_volume), True, (255, 255, 255))
        screen.blit(text_volume, (10, 90))

        # Actualizar la pantalla
        pygame.display.flip()

main()
import pygame
import random
import openai

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Definir tamaño de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego Sencillo")

# Definir posición inicial del jugador
posicion_jugador = [ANCHO_PANTALLA // 2, ALTO_PANTALLA - 50]

# Definir posición inicial de los enemigos
enemigos = []
for i in range(10):
    enemigos.append([random.randint(0, ANCHO_PANTALLA), random.randint(0, ALTO_PANTALLA // 2)])

# Definir tamaño de los enemigos
tamaño_enemigo = 25

# Definir velocidad del jugador
velocidad_jugador = 5

# Definir velocidad de los enemigos
velocidad_enemigo = 3

# Definir puntuación inicial
puntuacion = 0

# Crear fuente para mostrar la puntuación
fuente = pygame.font.SysFont("Arial", 30)

# Crear reloj para el juego
reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    # Manejar eventos de Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover jugador
    if teclas[pygame.K_LEFT] and posicion_jugador[0] > 0:
        posicion_jugador[0] -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and posicion_jugador[0] < ANCHO_PANTALLA - 50:
        posicion_jugador[0] += velocidad_jugador

    # Mover enemigos
    for i in range(len(enemigos)):
        enemigos[i][1] += velocidad_enemigo

        # Si el enemigo llega al fondo de la pantalla, volver a colocarlo al principio
        if enemigos[i][1] > ALTO_PANTALLA:
            enemigos[i][0] = random.randint(0, ANCHO_PANTALLA)
            enemigos[i][1] = random.randint(0, ALTO_PANTALLA // 2)

        # Si el jugador choca con un enemigo, terminar el juego
        if posicion_jugador[0] < enemigos[i][0] + tamaño_enemigo and posicion_jugador[0] + 50 > enemigos[i][0] and \
                posicion_jugador[1] < enemigos[i][1] + tamaño_enemigo and posicion_jugador[1] + 50 > enemigos[i][1]:
            jugando = False
            # Si el jugador toca un enemigo, incrementar la puntuación
            if posicion_jugador[0] < enemigos[i][0] + tamaño_enemigo and posicion_jugador[0] + 50 > enemigos[i][0] and \
                    posicion_jugador[1] < enemigos[i][1] + tamaño_enemigo and posicion_jugador[1] + 50 > enemigos[i][1]:
                puntuacion += 1
                enemigos[i][0] = random.randint(0, ANCHO_PANTALLA)
                enemigos[i][1] = random.randint(0, ALTO_PANTALLA // 2)

            # Limpiar pantalla
        pantalla.fill(BLANCO)

        # Dibujar jugador
        pygame.draw.rect(pantalla, NEGRO, (posicion_jugador[0], posicion_jugador[1], 50, 50))

        # Dibujar enemigos
        for i in range(len(enemigos)):
            pygame.draw.rect(pantalla, ROJO, (enemigos[i][0], enemigos[i][1], tamaño_enemigo, tamaño_enemigo))

        # Mostrar puntuación
        texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, NEGRO)
        pantalla.blit(texto_puntuacion, (10, 10))

        # Actualizar pantalla
        pygame.display.update()

        # Limitar FPS
        reloj.tick(60)

    # Terminar Pygame
    pygame.quit()

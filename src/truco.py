import pygame, sys
from pygame.locals import *
import os
from mazo import Mazo
from jugador import Jugador
from mesa import Mesa

#Constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

CARD_WIDTH = 150
CARD_HEIGHT = 270


pygame.init()
pygame.mixer.init()
card_down_sound = pygame.mixer.Sound(os.path.join("/home/valen1611/code/cartas/audio/card-mouse-down.wav"))
card_up_sound = pygame.mixer.Sound(os.path.join("/home/valen1611/code/cartas/audio/card-mouse-up.wav"))

flags = 0

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the fonts
font = pygame.font.SysFont('arial', 22)
button_font = pygame.font.SysFont('arial', 25)

highlights_color = (255, 255, 255)

# Set up the animation
animation_running = False
animation_speed = 1


# Cartas en mazo
carta_en_mano_1_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*1.5, SCREEN_HEIGHT*2/3, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_2_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT*2/3, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_3_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*1.5, SCREEN_HEIGHT*2/3, CARD_WIDTH, CARD_HEIGHT)

carta_en_mano_1_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*1.2, SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_2_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_3_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*1.2, SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)

cartas_en_mano_pos = [carta_en_mano_1_pos, carta_en_mano_2_pos, carta_en_mano_3_pos]
cartas_en_mano_pos_oponente = [carta_en_mano_1_pos_oponente, carta_en_mano_2_pos_oponente, carta_en_mano_3_pos_oponente]

def iniciar_mano():
    mazo = Mazo()
    p1 = Jugador('P1')
    p2 = Jugador('P2')
    cartas_p1, cartas_p2 = mazo.repartir()
    p1.recibir_cartas(cartas_p1)
    p2.recibir_cartas(cartas_p2)
    return p1, p2, mazo


def render_button(button, font, background_color, text, text_color, x, y, border_radius=0):
    pygame.draw.rect(DISPLAYSURF, background_color, button, border_radius=border_radius)
    DISPLAYSURF.blit(font.render(text, True, text_color), (button.x, button.y))



def mouse_dentro_carta(carta):
    if carta.x < pygame.mouse.get_pos()[0] < carta.x + carta.width and carta.y < pygame.mouse.get_pos()[1] < carta.y + carta.height:
        return True
    return False



def mensaje(texto):
    pygame.draw.rect(DISPLAYSURF, WHITE, (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, 200, 100))
    DISPLAYSURF.blit(font.render(texto, True, (0, 0, 0)), (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50))


def print_mesa(mesa, cartas_en_mesa):
    for i, carta in reversed(list(enumerate(mesa.cartas_jugadas))):
        if not carta:
            continue
        DISPLAYSURF.blit(carta.mostrar_img(), (cartas_en_mesa[i].x, cartas_en_mesa[i].y))
        DISPLAYSURF.blit(font.render(str(carta), True, BLACK), (cartas_en_mesa[i].x, cartas_en_mesa[i].y))
 

carta_atras = pygame.image.load("img_cartas/back.png")
carta_atras = pygame.transform.scale(carta_atras, (CARD_WIDTH, CARD_HEIGHT))


def mostrar_cartas(jugador, es_oponente):
    if es_oponente:
        for i in range(3):
            DISPLAYSURF.blit(carta_atras, (cartas_en_mano_pos_oponente[i].x, cartas_en_mano_pos_oponente[i].y))
    else:
        for i in range(3):
            DISPLAYSURF.blit(jugador.cartas[i].mostrar_imagen(), (cartas_en_mano_pos[i].x, cartas_en_mano_pos[i].y))



def puntos_display(jugador_1, jugador_2):
    pygame.draw.rect(DISPLAYSURF, WHITE, (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, 200, 100))

    puntos_p1 = jugador_1.puntos
    puntos_p2 = jugador_2.puntos
    DISPLAYSURF.blit(font.render(f'Puntos P1: {puntos_p1}', True, (0, 0, 0)), (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50))
    DISPLAYSURF.blit(font.render(f'Puntos P2: {puntos_p2}', True, (0, 0, 0)), (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 25))



def main():

    fondo = pygame.image.load("img/fondo.jpg")
    DISPLAYSURF.blit(fondo, (0, 0))
    

    gano = False
    fullscreen = False
    carta_seleccionada_surf = None

    p1, p2, mazo = iniciar_mano()
    jugador_actual = p1
    jugador_oponente = p2

    mouse_pressed1 = False
    mouse_pressed2 = False
    mouse_pressed3 = False
    bool_descartar = False
    arrastrando_carta = False
    repartir = False
    carta_seleccionada = None
    button_hovered = False
    texto_mensaje = ''
    while True:

        flags = 0
        
        if gano == True:
            break

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Toggle fullscreen mode
                    fullscreen = not fullscreen
                    if fullscreen:
                        flags = pygame.FULLSCREEN
                    else:
                        flags = 0

            

            if jugador_actual.gano(30):
                mensaje(f'Ganaste {jugador_actual.nombre}!')
                print(f'Ganaste {jugador_actual.nombre}!')
                gano = True
                break
            


            DISPLAYSURF.blit(fondo, (0, 0))
            
            mensaje(texto_mensaje)
            puntos_display(p1, p2)

            mostrar_cartas(jugador_actual, False)
            #mostrar_cartas(jugador_oponente, True)

            # drag cartas
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos(), "->", end="")
                if not event.button == 1:
                    continue

                for i, carta in enumerate(jugador_actual.cartas):
                    if cartas_en_mano_pos[i].collidepoint(event.pos):
                        arrastrando_carta = True
                        carta_seleccionada_surf = cartas_en_mano_pos[i]
                        carta_seleccionada = jugador_actual.cartas[i]
                    


                card_down_sound.play()
                

            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
                if not carta_seleccionada_surf: 
                    continue

                if event.button == 1:
                    #DISPLAYSURF.blit(fondo, (0, 0))
                    card_up_sound.play()    
                    carta_seleccionada_surf.center = pygame.mouse.get_pos()
                    # mouse_x, mouse_y = pygame.mouse.get_pos()
                    # but.x = mouse_x - CARD_WIDTH/2
                    # but.y = mouse_y - CARD_HEIGHT/2
                    arrastrando_carta = False
                    carta_seleccionada_surf = None
                   
                
            elif event.type == pygame.MOUSEMOTION and arrastrando_carta:
                carta_seleccionada_surf.center = pygame.mouse.get_pos()
               
        pygame.display.update()


main()
import pygame, sys
from pygame.locals import *
import os
from mazo import Mazo
from jugador import Jugador
from mesa import Mesa
from pygame_objs import *

# Set up pygame

pygame.mixer.init()
font = pygame.font.SysFont('arial', 22)

card_down_sound = pygame.mixer.Sound(("sound/card-mouse-down.wav"))
card_up_sound = pygame.mixer.Sound(("sound/card-mouse-up.wav"))

PARTIDASURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)


## Provisoria hasta tener la logica del juego real
def iniciar_mano():
    mazo = Mazo()
    p1 = Jugador('Camejo')
    p2 = Jugador('Senior Lotto')
    cartas_p1, cartas_p2 = mazo.repartir()
    p1.recibir_cartas(cartas_p1)
    p2.recibir_cartas(cartas_p2)
    return p1, p2, mazo



def mostrar_cartas(jugador, es_oponente):
    if es_oponente:
        for i in range(len(jugador.cartas)):
            PARTIDASURF.blit(carta_atras, (cartas_en_mano_pos_oponente[i].x, cartas_en_mano_pos_oponente[i].y))
    else:
        for i in range(len(jugador.cartas)):
            carta_aux = jugador.cartas[i].mostrar_imagen()
            carta_aux = pygame.transform.scale(carta_aux, (CARD_WIDTH, CARD_HEIGHT))
            carta = pygame.transform.rotate(carta_aux, 10 - i*10)
           
            PARTIDASURF.blit(carta, cartas_en_mano_pos[i])
            pygame.draw.rect(PARTIDASURF, BLUE, cartas_en_mano_pos[i], 3)

def mostrar_mesa(mesa):
    PARTIDASURF.blit(mesa_img, (mesa_pos.x, mesa_pos.y))
    pygame.draw.rect(PARTIDASURF, BLUE, mesa_pos, 3)

    for i in range(len(mesa.cartas_jugadas)):
        if not mesa.cartas_jugadas[i]:
            continue
        _carta_imagen = mesa.cartas_jugadas[i].mostrar_imagen()
        carta_imagen = pygame.transform.scale(_carta_imagen, (CARD_WIDTH, CARD_HEIGHT))
        PARTIDASURF.blit(carta_imagen, (cartas_en_mesa[i].x, cartas_en_mesa[i].y))
        pygame.draw.rect(PARTIDASURF, BLUE, cartas_en_mesa[i], 3)
    
def puntos_display(jugador_1, jugador_2):
    # Imagen
    PARTIDASURF.blit(hoja_puntos, (SCREEN_WIDTH/25, SCREEN_HEIGHT/25))

    # Cuadrados
    pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/20, SCREEN_HEIGHT/20, PICTURE_SIZE, PICTURE_SIZE), 3, 10)
    pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/20 + PICTURE_SIZE + 20, SCREEN_HEIGHT/20, PICTURE_SIZE, PICTURE_SIZE), 3, 10)
    
    # Nombres
    PARTIDASURF.blit(button_font.render(f'{jugador_1}', True, BLACK), (SCREEN_WIDTH/20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20))
    PARTIDASURF.blit(button_font.render(f'{jugador_2}', True, BLACK), (SCREEN_WIDTH/20 + PICTURE_SIZE + 20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20))

    # Puntos
    PARTIDASURF.blit(button_font.render(f'{jugador_1.puntos}', True, BLACK), (SCREEN_WIDTH/20 + 50, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20 + 50))
    PARTIDASURF.blit(button_font.render(f'{jugador_2.puntos}', True, BLACK), (SCREEN_WIDTH/20 + PICTURE_SIZE + 20 + 50, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20 + 50))

def botones_display():
    # Display y anuncio
    PARTIDASURF.blit(display, (SCREEN_WIDTH*(1-1/4), SCREEN_HEIGHT/25))
    PARTIDASURF.blit(coto, (SCREEN_WIDTH*(1-1/4) + 10, SCREEN_HEIGHT*6/10))
    
    # Botones
    render_boton(PARTIDASURF, truco_button_pos, 'Truco')
    render_boton(PARTIDASURF, envido_button_pos, 'Envido')
    render_boton(PARTIDASURF, flor_button_pos, 'Flor')
    render_boton(PARTIDASURF, quiero_button_pos, 'Quiero')
    render_boton(PARTIDASURF, no_quiero_button_pos, 'No Quiero')
    render_boton(PARTIDASURF, mazo_button_pos, 'Mazo')
    render_boton(PARTIDASURF, salir_button_pos, 'Salir')

def main():

    PARTIDASURF.blit(fondo, (0, 0))

    gano = False

    p1, p2, mazo = iniciar_mano()
    mesa = Mesa()
    jugador_actual = p1
    jugador_oponente = p2

    arrastrando_carta = False
    carta_seleccionada_surf = None
    carta_seleccionada = None


    while True:
        if gano == True:
            break

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if jugador_actual.gano(30):
                print(f'Ganaste {jugador_actual.nombre}!')
                gano = True
                break
            
            PARTIDASURF.blit(fondo, (0, 0))
            
            mostrar_mesa(mesa)
            puntos_display(p1, p2)
            botones_display()

            mostrar_cartas(jugador_actual, False)
            mostrar_cartas(jugador_oponente, True)

            
            # drag cartas
            if event.type == pygame.MOUSEBUTTONDOWN:
                card_down_sound.play()
                    
                if not event.button == 1:
                    continue

                for i, carta in enumerate(jugador_actual.cartas):
                    if cartas_en_mano_pos[i].collidepoint(event.pos):
                        arrastrando_carta = True
                        carta_seleccionada_surf = cartas_en_mano_pos[i]
                        offset_x = pygame.mouse.get_pos()[0] - carta_seleccionada_surf.centerx
                        offset_y = pygame.mouse.get_pos()[1] - carta_seleccionada_surf.centery
                        carta_seleccionada = jugador_actual.cartas[i]
                
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check si toco boton
                if truco_button_pos.collidepoint(event.pos):
                    print("Canto truco")
                elif envido_button_pos.collidepoint(event.pos):
                    print("Canto envido")
                elif flor_button_pos.collidepoint(event.pos):
                    print("Canto flor")
                elif quiero_button_pos.collidepoint(event.pos):
                    print("Quiero")
                elif no_quiero_button_pos.collidepoint(event.pos):
                    print("No quiero")
                elif mazo_button_pos.collidepoint(event.pos):
                    print("Mazo")
                elif salir_button_pos.collidepoint(event.pos):
                    print("Salir")
                
                if not carta_seleccionada_surf: 
                    continue
                
                # Check si jugo una carga
                if event.button == 1:
                    card_up_sound.play()

                    arrastrando_carta = False

                    if mesa_pos.collidepoint(event.pos):
                        jugador_actual.jugar_carta(carta_seleccionada)
                        cartas_en_mano_pos.remove(carta_seleccionada_surf)
                        mesa.recibirCarta(carta_seleccionada, jugador_actual)
                        print(f"carta {carta_seleccionada} en mesa")

                    carta_seleccionada_surf = None
                    carta_seleccionada = None
                
            elif event.type == pygame.MOUSEMOTION and arrastrando_carta:
                carta_seleccionada_surf.center = (pygame.mouse.get_pos()[0] - offset_x, pygame.mouse.get_pos()[1] - offset_y)
               
        pygame.display.update()

main()
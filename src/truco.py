import pygame, sys
from pygame.locals import *
import os
from mazo import Mazo
from jugador import Jugador
from mesa import Mesa
from logica import Partida
from pygame_objs import *
from time import sleep
import webbrowser

# Set up pygame

pygame.mixer.init()
font = pygame.font.SysFont('arial', 22)

card_down_sound = pygame.mixer.Sound(("sound/card-mouse-down.wav"))
card_up_sound = pygame.mixer.Sound(("sound/card-mouse-up.wav"))

PARTIDASURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
OFFSET_CARTA_Y = 50

## Provisoria hasta tener la logica del juego real
def iniciar_mano():
    p1 = Jugador('Camejo')
    p2 = Jugador('Senior Lotto')
    # cartas_p1, cartas_p2 = mazo.repartir()
    # p1.recibir_cartas(cartas_p1)
    # p2.recibir_cartas(cartas_p2)
    # return p1, p2, mazo
    mesa = Mesa()
    partida = Partida(p1, p2, 30, False, mesa)
    partida.iniciar_mano()
    return partida, mesa, p1, p2
    

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

def mostrar_mesa(mesa, jugador_actual):
    pygame.draw.rect(PARTIDASURF, BLACK, mesa_pos, 3)
    PARTIDASURF.blit(mesa_img, (mesa_pos.x+2, mesa_pos.y-2))


    for i in range(len(mesa.cartas_jugadas)):
        if not mesa.cartas_jugadas[i]:
            continue
        mano = mesa.cartas_jugadas[i] # [[(carta, jugador), (carta, jugador)], [(carta, jugador), (carta, jugador)]]
        
        tupla_ganadora = mano[0] # [(carta, jugador), (carta, jugador)]
        carta_ganadora = tupla_ganadora[0]              
        _carta_imagen_1 = carta_ganadora.mostrar_imagen() # (carta, jugador)
        carta_imagen_1 = pygame.transform.scale(_carta_imagen_1, (CARD_WIDTH, CARD_HEIGHT))

        mult = 1

        if len(mano) == 2:
            tupla_perdedora = mano[1] # [(carta, jugador), (carta, jugador)]
            if tupla_perdedora[1] != jugador_actual:
                mult = -1
            carta_perdedora = tupla_perdedora[0]
            _carta_imagen_2 = carta_perdedora.mostrar_imagen()
            carta_imagen_2 = pygame.transform.scale(_carta_imagen_2, (CARD_WIDTH, CARD_HEIGHT))
            
            PARTIDASURF.blit(carta_imagen_2, (cartas_en_mesa[i].x, cartas_en_mesa[i].y + (OFFSET_CARTA_Y * mult)))
            

        
        PARTIDASURF.blit(carta_imagen_1, (cartas_en_mesa[i].x, cartas_en_mesa[i].y + (OFFSET_CARTA_Y * mult * -1)))

def fosforitos(puntos, offset_jugador):
    if puntos > 25:
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50 + 75))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50 + 150))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50 + 225 + 25))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50 + 300 + 25))
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 375 + 25))
    elif puntos > 20:
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 75))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 150))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 225 + 25))
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 300 + 25))
    elif puntos > 15:
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 75))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 150))
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50 + 225 + 25))
    elif puntos > 10:
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE + 50))
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 75))
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 150))
    elif puntos > 5:
        PARTIDASURF.blit(fosforos_5, (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50))
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50 + 75))
    else:
        PARTIDASURF.blit(fosforos[puntos % 5 - 1], (SCREEN_WIDTH/20 + offset_jugador, SCREEN_HEIGHT/20 + PICTURE_SIZE  + 50))
        

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
    if jugador_1.puntos > 0:
        fosforitos(jugador_1.puntos, 0)
    if jugador_2.puntos > 0:
        fosforitos(jugador_2.puntos, PICTURE_SIZE + 20)


    PARTIDASURF.blit(button_font.render(f'{jugador_1.puntos}', True, BLACK), (SCREEN_WIDTH/20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20 + 50))
    PARTIDASURF.blit(button_font.render(f'{jugador_2.puntos}', True, BLACK), (SCREEN_WIDTH/20 + PICTURE_SIZE + 20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20 + 50))

def botones_display(se_puede_cantar_tantos, falta_envido_cantado, real_envio_cantado, envido_cantado):
    # Display y anuncio
    PARTIDASURF.blit(display, (SCREEN_WIDTH*(1-1/4), SCREEN_HEIGHT/25))
    PARTIDASURF.blit(coto, (SCREEN_WIDTH*(1-1/4) + 10, SCREEN_HEIGHT*6/10))
    # Botones
    render_boton(PARTIDASURF, truco_button_pos, 'Truco')

    render_boton(PARTIDASURF, envido_button_pos, 'Envido')
    render_boton(PARTIDASURF, real_envido_button_pos, 'Real Envido')
    render_boton(PARTIDASURF, falta_envido_button_pos, 'Falta Envido')
    render_boton(PARTIDASURF, flor_button_pos, 'Flor')

    if not se_puede_cantar_tantos:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, real_envido_button_pos, 'Real Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, falta_envido_button_pos, 'Falta Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, flor_button_pos, 'Flor', color_boton=GRAY)

    if falta_envido_cantado:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, real_envido_button_pos, 'Real Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, falta_envido_button_pos, 'Falta Envido', color_boton=GRAY)

    if real_envio_cantado:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, real_envido_button_pos, 'Real Envido', color_boton=GRAY)

    if envido_cantado:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)


    render_boton(PARTIDASURF, mazo_button_pos, 'Mazo')
    render_boton(PARTIDASURF, salir_button_pos, 'Salir')

def mostrar_cartel_turno(jugador_actual):
    pygame.draw.rect(PARTIDASURF, WHITE, turno_actual_cartel, border_radius=10)
    pygame.draw.rect(PARTIDASURF, BLACK, turno_actual_cartel, 3, 10)

    text_coords = (turno_actual_cartel.x + turno_actual_cartel.width/2 - 50, turno_actual_cartel.y + turno_actual_cartel.height/2 - 10)
    PARTIDASURF.blit(button_font.render(f'Turno de: {jugador_actual}', True, BLACK), text_coords)

def main():

    PARTIDASURF.blit(fondo, (0, 0))

    gano = False
    gano_ronda = False

    partida, mesa, p1, p2 = iniciar_mano() # WIP se puede pasar a clase para no tener todo al aire

    jugador_actual = p1
    jugador_oponente = p2

    arrastrando_carta = False
    carta_seleccionada_surf = None
    carta_seleccionada = None
    pos_original = None

    se_puede_cantar_tantos = True
    envido_cantado = False
    envido_envido_cantado = False
    real_envio_cantado = False
    falta_envido_cantado = False
    while True:
        if gano == True:
            break
        
       

        if gano_ronda:
            gano_ronda = False
            print('Alguien gano la ronda xd') #CArtelito: X jugador gano!
            sleep(2)
            #Borrar cartelito
            mesa = Mesa()
            partida.mesa = mesa
            partida.sumar_puntos_a_ganador()
            partida.iniciar_mano()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            jugador_actual = partida.obtener_jugador_actual()
            jugador_oponente = partida.obtener_jugador_contrario()
            
            PARTIDASURF.blit(fondo, (0, 0))
            
            mostrar_mesa(mesa, jugador_actual)
            puntos_display(p1, p2)
            botones_display(se_puede_cantar_tantos, falta_envido_cantado, real_envio_cantado, envido_cantado)

            mostrar_cartas(jugador_actual, False)
            mostrar_cartas(jugador_oponente, True)
            
            mostrar_cartel_turno(jugador_actual)

            if partida.envido_actual != None:
                # Botones de envido
                # draw a rect behin the buttons
                pygame.draw.rect(PARTIDASURF, BLUE, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), border_radius=10)
                pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), 3, 10)
                render_boton(PARTIDASURF, envido_quiero_button_pos, 'Quiero')
                render_boton(PARTIDASURF, envido_no_quiero_button_pos, 'No Quiero')


                render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido')
                render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido')
                render_boton(PARTIDASURF, envido_falta_envido_button_pos, 'Falta Envido')

                if envido_envido_cantado:
                    render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)

                if real_envio_cantado:
                    render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)
                    render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido', color_boton=GRAY)

                if falta_envido_cantado:
                    render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)
                    render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido', color_boton=GRAY)
                    render_boton(PARTIDASURF, envido_falta_envido_button_pos, 'Falta Envido', color_boton=GRAY)


            # drag cartas
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"cartas de {p1}: {p1.cartas} ")
                print(f"cartas de {p2}: {p2.cartas} ")

                card_down_sound.play()
                
                # Check si toco boton
                if truco_button_pos.collidepoint(event.pos):
                    print("Canto truco")

                
                elif envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado and not real_envio_cantado and not envido_envido_cantado:
                    print("Canto envido")
                    envido_cantado = True
                    partida.cantar_envido("ENVIDO")
                
                elif real_envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado and not real_envio_cantado:
                    print("Real Envido")
                    real_envio_cantado = True
                    partida.cantar_envido("REALENVIDO")

                elif falta_envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado:
                    print("Falta Envido")
                    falta_envido_cantado = True
                    partida.cantar_envido("FALTAENVIDO")

                elif flor_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado:
                    print("Canto flor")
                
                elif mazo_button_pos.collidepoint(event.pos):
                    display_cartel_envido(PARTIDASURF, res)
                    print("Mazo")
                elif salir_button_pos.collidepoint(event.pos):
                    print("Salir")
                

                # Check botones de envido
                if se_puede_cantar_tantos:
                    if envido_quiero_button_pos.collidepoint(event.pos):
                        print("Quiero envido")
                        res = partida.envido_actual.aceptar_envido()
                        res.ganador.sumar_puntos(res.puntos_a_sumar)
                        print(res)
                        se_puede_cantar_tantos = False
                        display_cartel_envido(PARTIDASURF, res)
                        partida._resetear_envido()


                    elif envido_no_quiero_button_pos.collidepoint(event.pos):
                        print("No quiero envido")
                        puntos = partida.envido_actual.rechazar_envido()
                        jugador_oponente.sumar_puntos(puntos)
                        se_puede_cantar_tantos = False
                        partida._resetear_envido()

                    elif envido_envido_button_pos.collidepoint(event.pos) and not falta_envido_cantado and not real_envio_cantado and not envido_envido_cantado:
                        print("Envido")
                        
                        envido_envido_cantado = True
                        partida.cantar_envido("ENVIDO")

                    elif envido_real_envido_button_pos.collidepoint(event.pos) and not falta_envido_cantado and not real_envio_cantado:
                        print("Real Envido")
                        
                        real_envio_cantado = True
                        partida.envido_actual.aceptar_envido()
                        partida.cantar_envido("REALENVIDO")

                    elif envido_falta_envido_button_pos.collidepoint(event.pos) and not falta_envido_cantado:
                        print("Falta Envido")
                        
                        falta_envido_cantado = True
                        partida.envido_actual.aceptar_envido()
                        partida.cantar_envido("FALTAENVIDO")

                    
                if coto_boton.collidepoint(event.pos):
                    webbrowser.open('https://youtu.be/uHgt8giw1LY')

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
                if not carta_seleccionada_surf: 
                    continue
                
                # Check si jugo una carta
                if event.button == 1:
                    card_up_sound.play()

                    arrastrando_carta = False

                    if mesa_pos.collidepoint(event.pos):
                        partida.jugar_carta(carta_seleccionada)
                        if p2 == jugador_actual:
                            se_puede_cantar_envido = False
                        
                        index = cartas_en_mano_pos.index(carta_seleccionada_surf)
                        
                        cartas_en_mano_pos.remove(carta_seleccionada_surf)
                        
                        nueva_x = cartas_en_mano_pos_originales[index][0]
                        nueva_y = cartas_en_mano_pos_originales[index][1]

                        nueva = pygame.Rect(nueva_x, nueva_y, CARD_WIDTH, CARD_HEIGHT)

                        cartas_en_mano_pos.insert(index, nueva)
                        
                        
                        print(f"se jugo {index} en mesa")
                        #cartas_en_mano_pos.remove(carta_seleccionada_surf)
                        print(f"carta {carta_seleccionada} en mesa")

                    
                        hay_ganador_ronda = partida.hay_ganador_ronda()
                        if hay_ganador_ronda:
                            gano_ronda = True
                    carta_seleccionada_surf = None
                    carta_seleccionada = None
                
            elif event.type == pygame.MOUSEMOTION and arrastrando_carta:
                carta_seleccionada_surf.center = (pygame.mouse.get_pos()[0] - offset_x, pygame.mouse.get_pos()[1] - offset_y)
               
        pygame.display.update()

main()
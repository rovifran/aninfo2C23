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

pygame.mixer.init()
font = pygame.font.SysFont('arial', 22)

card_down_sound = pygame.mixer.Sound(("sound/card-mouse-down.wav"))
card_up_sound = pygame.mixer.Sound(("sound/card-mouse-up.wav"))

PARTIDASURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
OFFSET_CARTA_Y = 50

## Provisoria hasta tener la logica del juego real
def iniciar_mano(nombre_jugador_1, nombre_jugador_2, puntos):
    p1 = Jugador(nombre_jugador_1)
    p2 = Jugador(nombre_jugador_2)
    # cartas_p1, cartas_p2 = mazo.repartir()
    # p1.recibir_cartas(cartas_p1)
    # p2.recibir_cartas(cartas_p2)
    # return p1, p2, mazo
    mesa = Mesa()
    partida = Partida(p1, p2, puntos, mesa)
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
    jugador_rect = pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/20, SCREEN_HEIGHT/20, PICTURE_SIZE, PICTURE_SIZE), 3, 10)
    imagen_jugador = pygame.transform.scale(fotos_pjs[jugador_1.personaje], (PICTURE_SIZE, PICTURE_SIZE))
    PARTIDASURF.blit(imagen_jugador, jugador_rect)

    riedel_rect = pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/20 + PICTURE_SIZE + 20, SCREEN_HEIGHT/20, PICTURE_SIZE, PICTURE_SIZE), 3, 10)
    imagen_riedel = pygame.transform.scale(fotos_pjs[jugador_2.personaje], (PICTURE_SIZE, PICTURE_SIZE))
    PARTIDASURF.blit(imagen_riedel, riedel_rect)
    
    # Nombres
    PARTIDASURF.blit(button_font.render(f'{jugador_1}', True, BLACK), (SCREEN_WIDTH/20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20))
    PARTIDASURF.blit(button_font.render(f'{jugador_2}', True, BLACK), (SCREEN_WIDTH/20 + PICTURE_SIZE + 20, SCREEN_HEIGHT/20 + PICTURE_SIZE + 20))

    # Puntos
    if jugador_1.puntos > 0:
        fosforitos(jugador_1.puntos, 0)
    if jugador_2.puntos > 0:
        fosforitos(jugador_2.puntos, PICTURE_SIZE + 20)


def botones_display(truco_actual, se_puede_cantar_truco, se_puede_cantar_tantos, falta_envido_cantado, real_envido_cantado, envido_cantado):
    # Display y anuncio
    PARTIDASURF.blit(display, (SCREEN_WIDTH*(1-1/4), SCREEN_HEIGHT/25))
    PARTIDASURF.blit(coto, (SCREEN_WIDTH*(1-1/4) + 10, SCREEN_HEIGHT*6/10))
    # Botones
    if se_puede_cantar_truco:
        render_boton(PARTIDASURF, truco_button_pos, truco_actual)

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

    if real_envido_cantado:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)
        render_boton(PARTIDASURF, real_envido_button_pos, 'Real Envido', color_boton=GRAY)

    if envido_cantado:
        render_boton(PARTIDASURF, envido_button_pos, 'Envido', color_boton=GRAY)


    render_boton(PARTIDASURF, mazo_button_pos, 'Mazo')
    render_boton(PARTIDASURF, salir_button_pos, 'Salir')

def mostrar_cartel_turno(jugador_actual):
    pygame.draw.rect(PARTIDASURF, WHITE, turno_actual_cartel, border_radius=10)
    pygame.draw.rect(PARTIDASURF, BLACK, turno_actual_cartel, 3, 10)

    text_coords = (turno_actual_cartel.x + turno_actual_cartel.width/2 - 90, turno_actual_cartel.y + turno_actual_cartel.height/2 - 10)
    PARTIDASURF.blit(button_font.render(f'Turno de: {jugador_actual}', True, BLACK), text_coords)

def reiniciar_pos_carta(carta_seleccionada_surf):
    index = cartas_en_mano_pos.index(carta_seleccionada_surf)
    cartas_en_mano_pos.remove(carta_seleccionada_surf)
    nueva_x = cartas_en_mano_pos_originales[index][0]
    nueva_y = cartas_en_mano_pos_originales[index][1]
    nueva = pygame.Rect(nueva_x, nueva_y, CARD_WIDTH, CARD_HEIGHT)
    cartas_en_mano_pos.insert(index, nueva)

def mostrar_opciones_truco(partida):
    if partida.truco_actual != None:
        # Botones de truco
        # draw a rect behin the buttons
        pygame.draw.rect(PARTIDASURF, BLUE, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), border_radius=10)
        pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), 3, 10)

        render_boton(PARTIDASURF, truco_quiero_button_pos, 'Quiero')
        render_boton(PARTIDASURF, truco_no_quiero_button_pos, 'No Quiero')
        render_boton(PARTIDASURF, truco_re_truco_button_pos, 'Re Truco', color_boton=GRAY)
        render_boton(PARTIDASURF, truco_vale_cuatro_button_pos, 'Vale Cuatro', color_boton=GRAY)
        
        if partida.jugador_actual.canto_truco_actual == "RETRUCO":
            render_boton(PARTIDASURF, truco_re_truco_button_pos, 'Re Truco')
        if partida.jugador_actual.canto_truco_actual == "VALE_CUATRO":
            render_boton(PARTIDASURF, truco_vale_cuatro_button_pos, 'Vale Cuatro')
        
        fase = partida.truco_actual.fase
        canto = fase.split("_")[-1].lower()
        message_display(partida.jugador_contrario.personaje + " canto " + canto, 35, 0)

def mostrar_opciones_envido(partida, envido_envido_cantado, real_envido_cantado, falta_envido_cantado):
     if partida.envido_actual != None:
        # Botones de envido
        pygame.draw.rect(PARTIDASURF, BLUE, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), border_radius=10)
        pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), 3, 10)
        render_boton(PARTIDASURF, envido_quiero_button_pos, 'Quiero')
        render_boton(PARTIDASURF, envido_no_quiero_button_pos, 'No Quiero')


        render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido')
        render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido')
        render_boton(PARTIDASURF, envido_falta_envido_button_pos, 'Falta Envido')

        if envido_envido_cantado:
            render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)

        if real_envido_cantado:
            render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)
            render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido', color_boton=GRAY)

        if falta_envido_cantado:
            render_boton(PARTIDASURF, envido_envido_button_pos, 'Envido', color_boton=GRAY)
            render_boton(PARTIDASURF, envido_real_envido_button_pos, 'Real Envido', color_boton=GRAY)
            render_boton(PARTIDASURF, envido_falta_envido_button_pos, 'Falta Envido', color_boton=GRAY)
        
        fase = partida.envido_actual.fase

        canto = "falta envido" if partida.envido_actual.es_falta_envido else fase.split("_")[-1].lower()

        message_display(partida.jugador_contrario.personaje + " cantó " + canto, 35, 0)

def mostrar_opciones_flor(partida):
    if partida.flor_actual != None: 
        pygame.draw.rect(PARTIDASURF, BLUE, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), border_radius=10)
        pygame.draw.rect(PARTIDASURF, BLACK, (SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH -10,SCREEN_HEIGHT/25 + 10-10, BUTTON_WIDTH*5+20, BUTTON_HEIGHT+20), 3, 10)
        
        render_boton(PARTIDASURF, flor_quiero_button_pos, 'Quiero')
        render_boton(PARTIDASURF, flor_no_quiero_button_pos, 'No Quiero')
        render_boton(PARTIDASURF, contraflor_quiero_button_pos, 'Contra Flor')
        
        fase = partida.flor_actual.obtener_fase()
        
        if fase == "Contra Flor":
            render_boton(PARTIDASURF, contraflor_quiero_button_pos, 'Contra Flor', color_boton=GRAY)
            
        message_display(partida.jugador_contrario.personaje + " canto " + fase, 35, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(mensaje, tamanio = 60, sleep_t = 0.75, cartel_t = 0):
    largeText = pygame.font.Font("freesansbold.ttf", tamanio)
    pygame.draw.rect(PARTIDASURF, WHITE, (SCREEN_WIDTH/2 - 200 - cartel_t, SCREEN_HEIGHT/2 - 50 - cartel_t, 400 + cartel_t*2, 100 + cartel_t*2), border_radius=10)

    TextSurf, TextRect = text_objects(mensaje, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    PARTIDASURF.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(sleep_t)

def check_ganador(partida):
    if partida.jugador_actual.puntos >= partida.max_puntos:
        return partida.jugador_actual
    elif partida.jugador_contrario.puntos >= partida.max_puntos:
        return partida.jugador_contrario
    return None

def init_partida(nombre_p1, nombre_p2, max_puntos):
    PARTIDASURF.blit(fondo, (0, 0))

    gano = False
    gano_ronda = False

    partida, mesa, p1, p2 = iniciar_mano(nombre_p1, nombre_p2, max_puntos) # WIP se puede pasar a clase para no tener todo al aire

    jugador_actual = p1
    jugador_oponente = p2
    
    arrastrando_carta = False
    carta_seleccionada_surf = None
    carta_seleccionada = None

    se_puede_cantar_truco = True
    se_canto_truco = False

    se_puede_cantar_tantos = True
    envido_cantado = False
    flor_cantada = False
    envido_envido_cantado = False
    real_envido_cantado = False
    falta_envido_cantado = False

    riedel_juega_por_primera_vez = True

    truco_etapas = ["VALE_CUATRO", "RETRUCO", "TRUCO"]

    truco_botones_a_etapas = {
        "TRUCO" : "Truco",
        "RETRUCO" : "Re Truco",
        "VALE_CUATRO" : "Vale Cuatro"
    }
    
    truco_music.play(50)

    while True:
        ganador = check_ganador(partida)
        if gano == True or ganador != None:
            puntos_display(p1, p2)
            message_display(f"{ganador.personaje} gano la partida!", 50, 5, 150)
            break
        
        se_puede_cantar_truco = True

        if gano_ronda:
            gano_ronda = False
            message_display("Gano la ronda " + partida.ganador_final_mano.personaje, 35, cartel_t=30)
            
            #Borrar cartelito
            mesa = Mesa()
            partida.mesa = mesa
            partida.sumar_puntos_a_ganador()
            
            se_puede_cantar_truco = True
            se_canto_truco = False

            jugador_oponente.canto_truco_actual = "TRUCO"
            jugador_actual.canto_truco_actual = "TRUCO"

            se_puede_cantar_tantos = True
            envido_cantado = False
            envido_envido_cantado = False
            real_envido_cantado = False
            falta_envido_cantado = False

            truco_etapas = ["VALE_CUATRO", "RETRUCO", "TRUCO"]

            partida.iniciar_mano()
            message_display("Turno de " + partida.jugador_actual.personaje, 35, cartel_t=30)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            jugador_actual = partida.obtener_jugador_actual()
            jugador_oponente = partida.obtener_jugador_contrario()
            
            if jugador_actual.canto_truco_actual == "-":
                se_puede_cantar_truco = False

            PARTIDASURF.blit(fondo, (0, 0))
            
            mostrar_mesa(mesa, jugador_actual)
            puntos_display(p1, p2)

            if truco_etapas == []:
                truco_actual_lindo = "-"
            else:
                truco_actual_lindo = truco_botones_a_etapas[truco_etapas[-1]]

            botones_display(truco_actual_lindo, se_puede_cantar_truco, se_puede_cantar_tantos, falta_envido_cantado, real_envido_cantado, envido_cantado)

            mostrar_cartas(jugador_actual, False)
            mostrar_cartas(jugador_oponente, True)
            
            mostrar_cartel_turno(jugador_actual)

            mostrar_opciones_envido(partida, envido_envido_cantado, real_envido_cantado, falta_envido_cantado)
            
            mostrar_opciones_flor(partida)
            
            if se_canto_truco:
                mostrar_opciones_truco(partida)

            # drag cartas
            if event.type == pygame.MOUSEBUTTONDOWN:
                card_down_sound.play()
                
                # Check si toco boton
                if truco_button_pos.collidepoint(event.pos) and se_puede_cantar_truco and jugador_actual.canto_truco_actual != "-":
                    truco_a_llamar = truco_etapas.pop()

                    if truco_etapas == []:
                        jugador_oponente.canto_truco_actual = "-"
                    else:
                        jugador_oponente.canto_truco_actual = truco_etapas[-1]
                    
                    jugador_actual.canto_truco_actual = "-"
                    

                    partida.cantar_truco(truco_a_llamar)
                    se_canto_truco  = True
                    se_puede_cantar_tantos = False

                elif envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado and not real_envido_cantado and not envido_envido_cantado:
                    envido_cantado = True
                    partida.cantar_envido("ENVIDO")
                
                elif real_envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado and not real_envido_cantado:
                    envido_cantado = True
                    real_envido_cantado = True
                    partida.cantar_envido("REALENVIDO")

                elif falta_envido_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado:
                    envido_cantado = True
                    falta_envido_cantado = True
                    partida.cantar_envido("FALTAENVIDO")

                elif flor_button_pos.collidepoint(event.pos) and se_puede_cantar_tantos and not falta_envido_cantado:
                    flor_cantada = True 
                    partida.cantar_flor()
                    #webbrowser.open('https://youtu.be/vdfCUkJRfxg')
                
                elif mazo_button_pos.collidepoint(event.pos):
                    message_display(jugador_actual.personaje + " se fue al mazo", 30, sleep_t=1.3, cartel_t=30)
                    if partida.truco_actual != None:
                        partida.truco_actual.aceptar_truco()

                    partida.ganador_final_mano = jugador_oponente
                    gano_ronda = True
                elif salir_button_pos.collidepoint(event.pos):
                    webbrowser.open('https://youtu.be/uHgt8giw1LY')
                    
                    return
                # Check botones flor 
                if se_puede_cantar_tantos and flor_cantada: 
                    if flor_quiero_button_pos.collidepoint(event.pos) and partida.flor_actual != None: 
                        res = partida.aceptar_flor() 
                        se_puede_cantar_tantos = False
                        message_display("Gano la flor " + res.ganador.personaje + " con " + str(res.puntos_ganador) + " puntos", 20, sleep_t=1.3, cartel_t=30)
                        message_display("Perdio la flor " + res.perdedor.personaje + " con " + str(res.puntos_perdedor) + " puntos", 20, sleep_t=1.3, cartel_t=30)
                    elif flor_no_quiero_button_pos.collidepoint(event.pos) and partida.flor_actual != None: 
                        se_puede_cantar_tantos = False 
                        puntos = partida.rechazar_flor() 
                        message_display(jugador_actual.personaje + " no quiso flor", 30, sleep_t=1.3, cartel_t=30)
                    
                    elif contraflor_quiero_button_pos.collidepoint(event.pos) and partida.flor_actual != None and partida.flor_actual.obtener_fase() != "Contra Flor": 
                        partida.cantar_flor() 
                        
                # Check botones de envido
                if se_puede_cantar_tantos and envido_cantado:
                    if envido_quiero_button_pos.collidepoint(event.pos) and partida.envido_actual != None:
                        res = partida.aceptar_envido()
                        se_puede_cantar_tantos = False
                        message_display("Gano el envido " + res.ganador.personaje + " con " + str(res.puntos_ganador) + " puntos", 20, sleep_t=1.3, cartel_t=30)
                        message_display("Perdio el envido " + res.perdedor.personaje + " con " + str(res.puntos_perdedor) + " puntos", 20, sleep_t=1.3, cartel_t=30)

                    elif envido_no_quiero_button_pos.collidepoint(event.pos) and partida.envido_actual != None:
                        puntos = partida.envido_actual.rechazar_envido()
                        jugador_oponente.sumar_puntos(puntos)
                        se_puede_cantar_tantos = False
                        message_display(jugador_actual.personaje + " no quiso el envido", 30, sleep_t=1.3, cartel_t=30)
                        partida._resetear_envido()

                    elif envido_envido_button_pos.collidepoint(event.pos) and partida.envido_actual != None and not falta_envido_cantado and not real_envido_cantado and not envido_envido_cantado:
                        
                        envido_envido_cantado = True
                        partida.cantar_envido("ENVIDO")

                    elif envido_real_envido_button_pos.collidepoint(event.pos) and partida.envido_actual != None and not falta_envido_cantado and not real_envido_cantado:
                        
                        real_envido_cantado = True
                        partida.envido_actual.aceptar_envido()
                        partida.cantar_envido("REALENVIDO")

                    elif envido_falta_envido_button_pos.collidepoint(event.pos) and partida.envido_actual != None and not falta_envido_cantado:
                        
                        falta_envido_cantado = True
                        partida.envido_actual.aceptar_envido()
                        partida.cantar_envido("FALTAENVIDO")

                if se_canto_truco:
                    if truco_quiero_button_pos.collidepoint(event.pos):
                        se_canto_truco = False
                        if truco_etapas == []:
                            jugador_oponente.canto_truco_actual = "-"
                        else:
                            jugador_oponente.canto_truco_actual = truco_etapas[-1]
                        jugador_oponente.canto_truco_actual = "-"
                        message_display(jugador_actual.personaje + " quiso", 30, sleep_t=1.3, cartel_t=30)
                        partida.aceptar_truco()
                        
                    elif truco_no_quiero_button_pos.collidepoint(event.pos):
                        message_display(jugador_actual.personaje + " no quiso", 30, sleep_t=1.3, cartel_t=30)

                        puntos = partida.truco_actual.rechazar_truco()
                        jugador_oponente.sumar_puntos(puntos-1)
                        se_canto_truco = False
                        partida.ganador_final_mano = jugador_oponente
                        gano_ronda = True
                    
                    elif truco_re_truco_button_pos.collidepoint(event.pos) and jugador_actual.canto_truco_actual == "RETRUCO":
                        truco_etapas.pop()
                        
                        jugador_oponente.canto_truco_actual = "VALE_CUATRO"
                        jugador_actual.canto_truco_actual = "-"
                        partida.cantar_truco("RETRUCO")
                        
                    elif truco_vale_cuatro_button_pos.collidepoint(event.pos) and jugador_actual.canto_truco_actual == "VALE_CUATRO":
                        jugador_actual.canto_truco_actual = "-"
                        truco_etapas.pop()
                        partida.cantar_truco("VALE_CUATRO")
                
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

                        if riedel_juega_por_primera_vez and jugador_actual == p2:
                            riedel_juega_por_primera_vez = False
                            sonidos_pjs["riedel"].play()

                        partida.jugar_carta(carta_seleccionada)


                        if p2 == jugador_actual:
                            se_puede_cantar_tantos = False
                        
                        reiniciar_pos_carta(carta_seleccionada_surf)
                                  
                        hay_ganador_ronda = partida.hay_ganador_ronda()
                        if hay_ganador_ronda:
                            gano_ronda = True
                            message_display("Turno de " + partida.jugador_actual.personaje, 35, cartel_t=30)
                    else:
                        reiniciar_pos_carta(carta_seleccionada_surf)

                    carta_seleccionada_surf = None
                    carta_seleccionada = None
                
            elif event.type == pygame.MOUSEMOTION and arrastrando_carta:
                carta_seleccionada_surf.center = (pygame.mouse.get_pos()[0] - offset_x, pygame.mouse.get_pos()[1] - offset_y)
               
        pygame.display.update()


















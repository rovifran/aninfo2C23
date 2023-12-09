import pygame
from pygame.locals import *

#Constantes
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

CARD_WIDTH = 150 * 6/10
CARD_HEIGHT = 270 * 6/10

PICTURE_SIZE = 100

#Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
pygame.init()
button_font = pygame.font.SysFont('arial', 18)


# Cartas
carta_en_mano_1_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*1, SCREEN_HEIGHT*3/4, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_2_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT*3/4, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_3_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*(1-1/3), SCREEN_HEIGHT*3/4, CARD_WIDTH, CARD_HEIGHT)

carta_en_mano_1_pos_og = (SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*1, SCREEN_HEIGHT*3/4)
carta_en_mano_2_pos_og = (SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT*3/4)
carta_en_mano_3_pos_og = (SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*(1-1/3), SCREEN_HEIGHT*3/4)

carta_en_mano_1_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*(2/3), SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_2_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)
carta_en_mano_3_pos_oponente = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*(2/3), SCREEN_HEIGHT/25, CARD_WIDTH, CARD_HEIGHT)

cartas_en_mano_pos = [carta_en_mano_1_pos, carta_en_mano_2_pos, carta_en_mano_3_pos]
cartas_en_mano_pos_originales = [carta_en_mano_1_pos_og, carta_en_mano_2_pos_og, carta_en_mano_3_pos_og]

cartas_en_mano_pos_oponente = [carta_en_mano_1_pos_oponente, carta_en_mano_2_pos_oponente, carta_en_mano_3_pos_oponente]

# Mesa
mesa_pos = pygame.Rect(SCREEN_WIDTH/3, SCREEN_HEIGHT*(1/3 - 1/10), SCREEN_WIDTH/3, SCREEN_HEIGHT/2)

carta_en_mesa_1_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 - CARD_WIDTH*1.2, SCREEN_HEIGHT/2 - CARD_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT)
carta_en_mesa_2_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2, SCREEN_HEIGHT/2 - CARD_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT)
carta_en_mesa_3_pos = pygame.Rect(SCREEN_WIDTH/2 - CARD_WIDTH/2 + CARD_WIDTH*1.2, SCREEN_HEIGHT/2 - CARD_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT)

cartas_en_mesa = [carta_en_mesa_1_pos, carta_en_mesa_2_pos, carta_en_mesa_3_pos]

# Botones
truco_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
envido_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 50, BUTTON_WIDTH, BUTTON_HEIGHT)
flor_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 100, BUTTON_WIDTH, BUTTON_HEIGHT)
quiero_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 150, BUTTON_WIDTH, BUTTON_HEIGHT)
no_quiero_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 200, BUTTON_WIDTH, BUTTON_HEIGHT)
mazo_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 250, BUTTON_WIDTH, BUTTON_HEIGHT)
salir_button_pos = pygame.Rect(SCREEN_WIDTH*(1-1/5) - 10, SCREEN_HEIGHT/25 + 10 + 300, BUTTON_WIDTH, BUTTON_HEIGHT)

turno_actual_cartel = pygame.Rect(SCREEN_WIDTH/25, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH*1.6, BUTTON_HEIGHT)

# Botones Envido
envido_quiero_button_pos = pygame.Rect(SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - 2*BUTTON_WIDTH,SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
envido_no_quiero_button_pos = pygame.Rect(SCREEN_WIDTH/2 - BUTTON_WIDTH/2 - BUTTON_WIDTH, SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
envido_envido_button_pos = pygame.Rect(SCREEN_WIDTH/2 - BUTTON_WIDTH/2, SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
envido_real_envido_button_pos = pygame.Rect(SCREEN_WIDTH/2 - BUTTON_WIDTH/2 + BUTTON_WIDTH, SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
envido_falta_envido_button_pos = pygame.Rect(SCREEN_WIDTH/2 - BUTTON_WIDTH/2 + 2*BUTTON_WIDTH, SCREEN_HEIGHT/25 + 10, BUTTON_WIDTH, BUTTON_HEIGHT)


def render_boton(surf, boton, texto, color_boton=WHITE):
    pygame.draw.rect(surf, color_boton, boton, border_radius=10)
    pygame.draw.rect(surf, BLACK, boton, 3, 10)
    
    text_coords = (boton.x + boton.width/2 - len(texto*4), boton.y + boton.height/2 - 10)
    surf.blit(button_font.render(texto, True, BLACK), text_coords)

# Imagenes
fondo = pygame.image.load("img/fondo.jpg")

carta_atras = pygame.image.load("img_cartas/back.png")
carta_atras = pygame.transform.scale(carta_atras, (CARD_WIDTH*3/4, CARD_HEIGHT*3/4))

display = pygame.image.load("img/display.png")
display = pygame.transform.rotate(display,90)

hoja_puntos = pygame.image.load("img/hoja.jpg")
hoja_puntos = pygame.transform.scale(hoja_puntos, (SCREEN_WIDTH*2/9, SCREEN_HEIGHT*(1-1/10)))

mesa_img = pygame.image.load("img/mesa.jpg")
mesa_img = pygame.transform.scale(mesa_img, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2))

coto = pygame.image.load("img/coto.png")
coto = pygame.transform.scale(coto, (SCREEN_WIDTH/5, SCREEN_HEIGHT/3))  
coto_boton = pygame.Rect(SCREEN_WIDTH*(1-1/4) + 10, SCREEN_HEIGHT*6/10, SCREEN_WIDTH/5, SCREEN_HEIGHT/3)

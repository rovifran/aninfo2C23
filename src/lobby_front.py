import pygame
from lobby import Lobby
pygame.init()
from pygame_objs import *

fondo = pygame.image.load("img/fondo.jpg")

img_boton = pygame.image.load("img/boton.png")


#botonsito
class TextHolder:
    def __init__(self, x, y, width, height, str, color):
        self.str = str
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, pygame_screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.str, True, self.color)
        pygame_screen.blit(text, self.rect)

    def is_clicked(self, pos):
        return False


class Button:
    def __init__(self, x, y, width, height, color, text, action, img=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action
        self.text = text
        self.img = img

    def draw(self, pygame_screen):
        
        scaled_img = pygame.transform.scale(fotos_pjs.get(self.img, img_boton), (self.rect.width, self.rect.height))
        
        pygame_screen.blit(scaled_img, self.rect)
        font = pygame.font.Font(None, 512//5)
        text = font.render(self.text, True, (49,23,17))
        x = self.rect.x
        y = self.rect.y
        w = self.rect.width
        h = self.rect.height
        
        text_rect = pygame.Rect(x + w * 0.2, y + h * 0.1, w * 0.6, h * 0.8)
        
        pygame_screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Screen: 
    def __init__(self, widgets):
        self.pygame_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.widgets = widgets
        self.lobby = Lobby()
        self.running = True
        self.starting = False

        self.lobby.seleccionar_personaje("mariachi")
        self.lobby.seleccionar_personaje_oponente("riedel")

    def start_match(self):
        self.running = False
        self.starting = True

    def is_running(self):
        return self.running

    def stop(self):
        print("dejo de correrse")
        self.running = False

    def click(self, event_pos):
        for widget in self.widgets:
            if widget.is_clicked(event_pos):
                widget.action()

    def display(self):
        self.pygame_screen.blit(fondo, (0, 0))
        for widget in self.widgets:
            widget.draw(self.pygame_screen)
        pygame.display.flip()

    def change_widgets(self, new_widgets):
        self.widgets = new_widgets

    def set_amt_points(self, amt):
        self.lobby.seleccionar_puntos(amt)

    def setPlayers(self, p1, p2):
        self.lobby.seleccionar_personaje(p1)
        self.lobby.seleccionar_personaje_oponente(p2)

    def set_flor(self, se_juega_con_flor):
        pass

    def set_oponente(self, oponente):
        self.lobby.seleccionar_personaje_oponente(oponente)

jugar_como_fito = Button(150, 150, 200, 200, (255, 0, 0), "" ,lambda : (sonidos_pjs["fito"].play(), screen.setPlayers("fito", "riedel"), screen.start_match()), img = "fito")
jugar_como_bob = Button(400, 150, 200, 200, (255, 0, 0), "" ,lambda : (sonidos_pjs["bob"].play(), screen.setPlayers("bob", "riedel"), screen.start_match()), img = "bob")
jugar_como_mariachi = Button(650, 150, 200, 200, (255, 0, 0), "" ,lambda : (sonidos_pjs["mariachi"].play(), screen.setPlayers("mariachi", "riedel"), screen.start_match()), img = "mariachi")
jugar_como_martu = Button(275, 400, 200, 200, (255, 0, 0), "" ,lambda : (sonidos_pjs["martu"].play(), screen.setPlayers("martu", "riedel"), screen.start_match()), img = "martu")
jugar_como_kim = Button(525, 400, 200, 200, (255, 0, 0), "" ,lambda : (sonidos_pjs["kim-jong-un"].play(), screen.setPlayers("kim-jong-un", "riedel"), screen.start_match()), img = "kim-jong-un")
play_game = TextHolder(20,100, 600, 150, "Choose your fighter:", (255,255,255))


widgets_for_screen_3 = [
    jugar_como_fito,
    jugar_como_bob,
    jugar_como_mariachi,
    jugar_como_martu,
    jugar_como_kim,
    play_game
]



popup_button = Button(100, 100, 400, 100, (0, 255, 0), "Jugar", lambda: play_screen(screen))
quit_button = Button(100, 250, 400, 100, (255, 0, 0), "Salir" , lambda: (screen.stop(), pygame.quit()))
widgets_for_screen_1 = [quit_button, popup_button]

hasta_15 = Button(100, 100, 400, 100, (0, 255, 0), "   a 15", lambda: (screen.set_amt_points(15), screen.change_widgets(widgets_for_screen_3)))
hasta_30 = Button(100, 250, 400, 100, (0, 255, 0), "   a 30", lambda: (screen.set_amt_points(30), screen.change_widgets(widgets_for_screen_3)))
widgets_for_screen_2 = [hasta_15, hasta_30]


screen = Screen(widgets_for_screen_1)

def return_to_menu():
    screen.change_widgets(widgets_for_screen_2)
    truco_music.stop()
    screen.starting = False
    screen.running = True
    screen.display()
    


def play_screen(screen):
    screen.change_widgets(widgets_for_screen_2)


def lobby_main():
    while True:
        lobby_music.play()
        while screen.is_running():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.click(event.pos)
            if screen.is_running():
                screen.display()

        if (screen.starting == True):
            lobby_music.stop()
            screen.lobby.iniciar_partida()

        




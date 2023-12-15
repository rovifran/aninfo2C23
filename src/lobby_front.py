import pygame
pygame.init()

fondo = pygame.image.load("img/fondo.jpg")
img_boton = pygame.image.load("img/boton.png")


#botonsito
class Button:
    def __init__(self, x, y, width, height, color, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action
        self.text = text

    def draw(self, pygame_screen):
        scaled_img = pygame.transform.scale(img_boton, (self.rect.width, self.rect.height))
        pygame_screen.blit(scaled_img, self.rect)
        # pygame.draw.rect(pygame_screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0,0,0))
        x = self.rect.x
        y = self.rect.y
        w = self.rect.width
        h = self.rect.height
        text_rect = pygame.Rect(x + w * 0.2, y + h * 0.2, w * 0.6, h * 0.6)
        pygame_screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

sin_flor = Button(100, 100, 200, 50, (255, 0, 0), "Sin flor" ,lambda : (screen.set_flor(False), screen.start_match()))
con_flor = Button(400, 100, 200, 50, (0, 255, 0), "Con flor", lambda: (screen.set_flor(True), screen.start_match()))
widgets_for_screen_3 = [sin_flor, con_flor]

quit_button = Button(100, 100, 200, 50, (255, 0, 0), "Salir" , lambda: (screen.stop(), pygame.quit()))
popup_button = Button(400, 100, 200, 50, (0, 255, 0), "Jugar", lambda: play_screen(screen, "Enter a number:", 0, lambda x: print(f"You entered {x}")))
widgets_for_screen_1 = [quit_button, popup_button]

hasta_15 = Button(100, 100, 200, 50, (0, 255, 0), "a 15", lambda: (screen.set_amt_players(15), screen.change_widgets(widgets_for_screen_3)))
hasta_30 = Button(400, 100, 200, 50, (0, 255, 0), "a 30", lambda: (screen.set_amt_players(30), screen.change_widgets(widgets_for_screen_3)))
widgets_for_screen_2 = [hasta_15, hasta_30]




#para que aparezca una ventanita que te pida las cosas necesarias para jugar
def play_screen(screen, question, default_value, action):
    print("hola")
    screen.change_widgets(widgets_for_screen_2)
    # pygame.draw.rect(screen, (255, 255, 255), (200, 200, 400, 200))
    # font = pygame.font.Font(None, 36)
    # text = font.render(question, True, (0, 0, 0))
    # screen.blit(text, (210, 210))
    # text = font.render(str(default_value), True, (0, 0, 0))
    # screen.blit(text, (210, 250))


class Screen: 
    def __init__(self, widgets):
        self.pygame_screen = pygame.display.set_mode((800, 600))
        self.widgets = widgets
        self.game_config = {"#jugadores": 15, "flor": False, "oponente": "sr lotto (el te conoce)"}
        self.running = True
        self.starting = False

    def start_match(self):
        self.running = False
        self.starting = True

    def is_running(self):
        return self.running

    def stop(self):
        self.running = False

    def click(self, event_pos):
        for widget in self.widgets:
            if widget.is_clicked(event_pos):
                widget.action()

    def display(self):
        # self.pygame_screen.fill((0, 0, 0))
        self.pygame_screen.blit(fondo, (0, 0))

        for widget in self.widgets:
            widget.draw(self.pygame_screen)
        pygame.display.flip()

    def change_widgets(self, new_widgets):
        self.widgets = new_widgets

    def set_amt_players(self, amt):
        self.game_config["#jugadores"] = amt

    def set_flor(self, se_juega_con_flor):
        self.game_config["flor"] = se_juega_con_flor

    def set_oponente(self, oponente):
        self.game_config["oponente"] = oponente





screen = Screen(widgets_for_screen_1)

running = True
while screen.is_running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.click(event.pos)
            # if quit_button.is_clicked(event.pos):
                # quit_button.action()
            # elif popup_button.is_clicked(event.pos):
                # popup_button.action()
    if screen.is_running():
        screen.display()

if (screen.starting == True):
    print(screen.game_config)
#    quit_button.draw(screen)
#    popup_button.draw(screen)


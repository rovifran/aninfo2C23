
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

from lobby_front import lobby_main

def main():
    print("Bienvenido a Truco Argentino")
    lobby_main()

main()



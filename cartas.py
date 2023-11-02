from typing import Tuple
from enum import Enum

import pygame
from pygame.locals import *
import os
import sys

CUR_DIR = os.getcwd()

PRIORIDAD_ANCHO_DE_ESPADA = 1
PRIORIDAD_ANCHO_DE_BASTO = 2
PRIORIDAD_SIETE_DE_ESPADA = 3
PRIORIDAD_SIETE_DE_ORO = 4
PRIORIDAD_TRES = 5
PRIORIDAD_DOS = 6
PRIORIDAD_ANCHO_FALSO = 7
PRIORIDAD_DOCE = 8
PRIORIDAD_ONCE = 9
PRIORIDAD_DIEZ = 10
PRIORIDAD_SIETE_FALSO = 11
PRIORIDAD_SEIS = 12
PRIORIDAD_CINCO = 13
PRIORIDAD_CUATRO = 14

def obtener_palo_y_numero(ruta_imagen: str) -> Tuple:
    numero, palo = ruta_imagen.split('.')[0].split('_')
    return int(numero), palo

class _Carta:
    def __init__(self, ruta_imagen: str, prioridad: int) -> None:
        numero, palo = obtener_palo_y_numero(ruta_imagen)
        self.numero = numero
        self.palo = palo
        self._prioridad = prioridad
        self.imagen = pygame.image.load(CUR_DIR + '/cartas/' + ruta_imagen)

    def carta(self):
        return type(self).__name__

    def mostrar_imagen(self) -> pygame.Surface:
        return self.imagen

    def __gt__(self, otra: '_Carta') -> bool:
        return self._prioridad < otra._prioridad
    
    def __ge__(self, otra: '_Carta') -> bool:
        return self._prioridad <= otra._prioridad
    
    def __eq__(self, otra: '_Carta') -> bool:
        return self._prioridad == otra._prioridad
    
    def __lt__(self, otra: '_Carta') -> bool:
        return self._prioridad > otra._prioridad
    
    def __le__(self, otra: '_Carta') -> bool:
        return self._prioridad >= otra._prioridad

class AnchoDeEspada(_Carta):
    
    def __init__(self, ruta: str) -> None: 
        super().__init__(ruta, PRIORIDAD_ANCHO_DE_ESPADA)

class AnchoDeBasto(_Carta):

    def __init__(self, ruta: str) -> None: 
        super().__init__(ruta, PRIORIDAD_ANCHO_DE_BASTO)
    
class SieteDeEspada(_Carta):

    def __init__(self, ruta: str) -> None:
      super().__init__(ruta, PRIORIDAD_SIETE_DE_ESPADA)

class SieteDeOro(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_SIETE_DE_ORO)

class Tres(_Carta):
    
    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_TRES)

class Dos(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_DOS)

class AnchoFalso(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_ANCHO_FALSO)

class Doce(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_DOCE)

class Once(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_ONCE)

class Diez(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_DIEZ)

class SieteFalso(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_SIETE_FALSO)

class Seis(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_SEIS)

class Cinco(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_CINCO)

class Cuatro(_Carta):

    def __init__(self, ruta: str) -> None:
        super().__init__(ruta, PRIORIDAD_CUATRO)

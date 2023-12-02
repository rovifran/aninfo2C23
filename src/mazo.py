import random

from cartas import *
from typing import Tuple, List


class Mazo():
    """
    Clase que representa un mazo de cartas españolas para jugar al Truco
    Es la encaregada de instanciar las 40 cartas del mazo, asi como también de mezclarlas y repartirlas

    Atributos:
        - cartas: Es una lista que contiene las instancias de las 40 cartas del mazo
    """

    def __init__(self) -> None:
        """
        Crea un mazo de cartas de truco, para ello instancia cada una de las 40 cartas del mazo
        con su respectiva ruta para cada una.
        
        PostCondiciones:
            - Crea un mazo de 40 cartas de truco, sin un orden en particular
        """

        self.cartas = [
            AnchoDeEspada("1_esp.png"),
            AnchoDeBasto("1_bas.png"),
            SieteDeEspada("7_esp.png"),
            SieteDeOro("7_oro.png"),
            AnchoFalso("1_oro.png"),
            AnchoFalso("1_copa.png"),
            SieteFalso("7_bas.png"),
            SieteFalso("7_copa.png"),
            Dos("2_esp.png"),
            Dos("2_bas.png"),
            Dos("2_oro.png"),
            Dos("2_copa.png"),
            Tres("3_esp.png"),
            Tres("3_bas.png"),
            Tres("3_oro.png"),
            Tres("3_copa.png"),
            Doce("12_esp.png"),
            Doce("12_bas.png"),
            Doce("12_oro.png"),
            Doce("12_copa.png"),
            Once("11_esp.png"),
            Once("11_bas.png"),
            Once("11_oro.png"),
            Once("11_copa.png"),
            Diez("10_esp.png"),
            Diez("10_bas.png"),
            Diez("10_oro.png"),
            Diez("10_copa.png"),
            Seis("6_esp.png"),
            Seis("6_bas.png"),
            Seis("6_oro.png"),
            Seis("6_copa.png"),
            Cinco("5_esp.png"),
            Cinco("5_bas.png"),
            Cinco("5_oro.png"),
            Cinco("5_copa.png"),
            Cuatro("4_esp.png"),
            Cuatro("4_bas.png"),
            Cuatro("4_oro.png"),
            Cuatro("4_copa.png")
        ]

    def mezclar(self) -> None:
        """
        Mezcla las cartas del mazo de forma aleatoria

        PostCondiciones:
            - Las cartas del mazo quedan mezcladas
        """
        random.shuffle(self.cartas)
    
    def repartir(self) -> Tuple[List["Carta"], List["Carta"]]:
        """
        Reparte las cartas del mazo en dos manos de 3 cartas cada una

        PostCondiciones:
            - Se devuelven dos listas de 3 cartas cada una
        """
        return self.cartas[0:3], self.cartas[3:6]

    def mezclar_y_repartir(self) -> Tuple[List["Carta"], List["Carta"]]:
        """
        Mezcla y reparte las cartas del mazo, devolviendo dos listas de 3 cartas cada una

        PostCondiciones:
            - Se devuelven dos listas de 3 cartas cada una, y el mazo queda mezclado
        """
        self.mezclar()
        return self.repartir()
"""
cmd = "Mazo()"

res = timeit.timeit(stmt=cmd, setup="from __main__ import Mazo", number=100)

print(res)
"""

""" 
mazo = Mazo()

for i in range(10):
    print(f"Mano {i}: {mazo.mezclar_y_repartir()}")
 """

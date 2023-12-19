import sys

sys.path.append('../')

from cartas import *
from jugador import Jugador


def test_1_jugador_juega_cartas_repetidas_correctamente_primero_izquierda():
    c1 = Tres("3_esp.png")
    c2 = Tres("3_bas.png")
    c3 = Tres("3_oro.png")

    j1 = Jugador("1")
    j1.recibir_cartas([c1, c2, c3])

    assert j1.obtener_cartas() == [c1, c2, c3]

    assert j1.jugar_carta(c1) == c1
    assert j1.obtener_cartas() == [c2, c3]

    assert j1.jugar_carta(c2) == c2
    assert j1.obtener_cartas() == [c3]

    assert j1.jugar_carta(c3) == c3
    assert j1.obtener_cartas() == []


def test_2_jugador_juega_cartas_repetidas_correctamente_primero_derecha():
    c1 = Tres("3_esp.png")
    c2 = Tres("3_bas.png")
    c3 = Tres("3_oro.png")

    j1 = Jugador("1")
    j1.recibir_cartas([c1, c2, c3])

    assert j1.obtener_cartas() == [c1, c2, c3]

    assert j1.jugar_carta(c3) == c3
    assert j1.obtener_cartas() == [c1, c2]

    assert j1.jugar_carta(c2) == c2
    assert j1.obtener_cartas() == [c1]

    assert j1.jugar_carta(c1) == c1
    assert j1.obtener_cartas() == []


def main():
    print("Corriendo tests de jugador...")
    test_1_jugador_juega_cartas_repetidas_correctamente_primero_izquierda()
    test_2_jugador_juega_cartas_repetidas_correctamente_primero_derecha()
    print("Todos los tests de jugador pasaron exitosamente!")


if __name__ == '__main__':
    main()

import sys

sys.path.append('../')

ENVIDO = "ENVIDO"
REAL_ENVIDO = "REALENVIDO"
FALTA_ENVIDO = "FALTAENVIDO"
ENVIDO_ENVIDO = "ENVIDO_ENVIDO"
ENVIDO_REAL_ENVIDO = "ENVIDO_REALENVIDO"
ENVIDO_ENVIDO_REAL_ENVIDO = "ENVIDO_ENVIDO_REALENVIDO"
MAX_PUNTOS = 30

from cartas import *
from envido import *
from jugador import Jugador


def test_1_envido_con_dos_y_tres_cartas_comunes_de_mismo_palo():
    j1 = Jugador('1')
    j2 = Jugador('2')

    c11 = SieteFalso("7_bas.png")
    c12 = Seis("6_bas.png")
    c13 = Cuatro("4_esp.png")

    c21 = SieteFalso("7_copa.png")
    c22 = Cinco("5_copa.png")
    c23 = Cuatro("4_copa.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, ENVIDO, MAX_PUNTOS)
    resultado = envido._comparar_tantos()

    assert (resultado.puntos_ganador == 33)
    assert (resultado.puntos_perdedor == 32)
    assert (resultado.puntos_a_sumar == 2)
    assert (resultado.ganador == j1)
    assert (resultado.perdedor == j2)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 1)


def test_2_real_envido_con_cartas_de_distinto_palo():
    j1 = Jugador('1')
    j2 = Jugador('2')

    c11 = AnchoDeEspada("1_esp.png")
    c12 = Seis("6_bas.png")
    c13 = Cuatro("4_copa.png")

    c21 = SieteFalso("7_copa.png")
    c22 = Tres("3_oro.png")
    c23 = Cuatro("4_bas.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, REAL_ENVIDO, MAX_PUNTOS)
    resultado = envido._comparar_tantos()

    assert (resultado.puntos_ganador == 7)
    assert (resultado.puntos_perdedor == 6)
    assert (resultado.puntos_a_sumar == 3)
    assert (resultado.ganador == j2)
    assert (resultado.perdedor == j1)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 1)


def test_3_envido_envido_con_cartas_negras():
    j1 = Jugador('1')
    j2 = Jugador('2')

    c11 = Doce("12_esp.png")
    c12 = Once("11_bas.png")
    c13 = Diez("10_copa.png")

    c21 = Doce("12_copa.png")
    c22 = Once("11_copa.png")
    c23 = Diez("10_esp.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, ENVIDO_ENVIDO, MAX_PUNTOS)
    resultado = envido._comparar_tantos()

    assert (resultado.puntos_ganador == 20)
    assert (resultado.puntos_perdedor == 0)
    assert (resultado.puntos_a_sumar == 4)
    assert (resultado.ganador == j2)
    assert (resultado.perdedor == j1)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 2)


def test_4_envido_envido_real_envido_con_puntos_iguales_es_parda():
    j1 = Jugador('1')
    j2 = Jugador('2')

    c11 = SieteFalso("7_copa.png")
    c12 = Tres("3_copa.png")
    c13 = Cuatro("4_bas.png")

    c21 = SieteFalso("7_esp.png")
    c22 = Tres("3_esp.png")
    c23 = Cuatro("4_oro.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, ENVIDO_ENVIDO_REAL_ENVIDO, MAX_PUNTOS)
    resultado = envido._comparar_tantos()

    assert (resultado.puntos_ganador == 30)
    assert (resultado.puntos_perdedor == 30)
    assert (resultado.puntos_a_sumar == 7)
    assert (resultado.ganador == None)
    assert (resultado.perdedor == None)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 3)


def test_5_falta_envido_suma_puntos_restantes():
    j1 = Jugador('1')
    j2 = Jugador('2')

    j1.puntos = 20

    c11 = AnchoDeEspada("1_esp.png")
    c12 = Seis("6_bas.png")
    c13 = Cuatro("4_copa.png")

    c21 = SieteFalso("7_copa.png")
    c22 = Tres("3_oro.png")
    c23 = Cuatro("4_bas.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, FALTA_ENVIDO, MAX_PUNTOS)
    resultado = envido.aceptar_envido()

    assert (resultado.puntos_ganador == 7)
    assert (resultado.puntos_perdedor == 6)
    assert (resultado.puntos_a_sumar == 10)
    assert (resultado.ganador == j2)
    assert (resultado.perdedor == j1)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 1)


def test_6_envido_falta_envido_suma_puntos_restantes():
    j1 = Jugador('1')
    j2 = Jugador('2')

    j1.puntos = 20

    c11 = AnchoDeEspada("1_esp.png")
    c12 = Seis("6_bas.png")
    c13 = Cuatro("4_copa.png")

    c21 = SieteFalso("7_copa.png")
    c22 = Tres("3_oro.png")
    c23 = Cuatro("4_bas.png")

    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])

    envido = Envido(j1, j2, ENVIDO, MAX_PUNTOS)
    envido.actualizar(FALTA_ENVIDO)
    resultado = envido.aceptar_envido()

    assert (resultado.puntos_ganador == 7)
    assert (resultado.puntos_perdedor == 6)
    assert (resultado.puntos_a_sumar == 10)
    assert (resultado.ganador == j2)
    assert (resultado.perdedor == j1)

    puntos_no_queridos = envido.rechazar_envido()
    assert (puntos_no_queridos == 3)


def main():
    print("\nTesteando envido...\n")

    test_1_envido_con_dos_y_tres_cartas_comunes_de_mismo_palo()
    test_2_real_envido_con_cartas_de_distinto_palo()
    test_3_envido_envido_con_cartas_negras()
    test_4_envido_envido_real_envido_con_puntos_iguales_es_parda()
    test_5_falta_envido_suma_puntos_restantes()
    test_6_envido_falta_envido_suma_puntos_restantes()

    print("\x1b[32mTodos los tests de envido pasaron exitosamente!\x1b[0m")


if __name__ == "__main__":
    main()

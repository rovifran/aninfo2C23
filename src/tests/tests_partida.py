import sys

sys.path.append('../')

from logica import Partida
from mesa import Mesa


def test_1_se_cambia_de_turno_correctamente():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    assert partida.jugador_actual == "Jugador 1"
    assert partida.jugador_contrario == "Jugador 2"
    partida.cambiar_turno()
    assert partida.jugador_actual == "Jugador 2"
    assert partida.jugador_contrario == "Jugador 1"
    partida.cambiar_turno()
    assert partida.jugador_actual == "Jugador 1"
    assert partida.jugador_contrario == "Jugador 2"
    print("Test 1 de partida paso exitosamente!")


def test_2_el_mismo_jugador_gana_dos_manos_seguidas():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = ["Jugador 1", "Jugador 1"]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 1"
    print("Test 2 de partida paso exitosamente!")


def test_3_el_mismo_jugador_gana_en_tercera_mano_sin_parda():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = ["Jugador 1", "Jugador 2", "Jugador 1"]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 1"
    print("Test 3 de partida paso exitosamente!")


def test_4_el_mismo_jugador_gana_en_tercera_mano_con_parda():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = ["Jugador 1", "Jugador 2", None]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 1"
    print("Test 4 de partida paso exitosamente!")


def test_5_gana_jugador_mano_por_triple_parda():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = [None, None, None]
    partida.definir_ganador()

    assert partida.ganador_final_mano == partida.jugador_mano
    print("Test 5 de partida paso exitosamente!")


def test_6_parda_solo_en_primera_mano():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = [None, "Jugador 2"]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 2"
    print("Test 6 de partida paso exitosamente!")


def test_7_parda_solo_en_segunda_mano():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = ["Jugador 1", None]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 1"
    print("Test 7 de partida paso exitosamente!")


def test_8_gana_en_tercera_mano_por_doble_parda():
    partida = Partida("Jugador 1", "Jugador 2", 15, mesa=Mesa())
    partida.ganador_por_mano = [None, None, "Jugador 2"]
    partida.definir_ganador()
    assert partida.ganador_final_mano == "Jugador 2"
    print("Test 8 de partida paso exitosamente!")


def main_test_partida():
    print("Corriendo tests de partida...")
    test_1_se_cambia_de_turno_correctamente()
    test_2_el_mismo_jugador_gana_dos_manos_seguidas()
    test_3_el_mismo_jugador_gana_en_tercera_mano_sin_parda()
    test_4_el_mismo_jugador_gana_en_tercera_mano_con_parda()
    test_5_gana_jugador_mano_por_triple_parda()
    test_6_parda_solo_en_primera_mano()
    test_7_parda_solo_en_segunda_mano()
    test_8_gana_en_tercera_mano_por_doble_parda()
    print("\x1b[32mTodos los tests de partida pasaron exitosamente!\x1b[0m")


if __name__ == '__main__':
    main_test_partida()

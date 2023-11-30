import sys
sys.path.append('../')

from mazo import Mazo

ITERACIONES_MANOS = 100

def test_1_mazo_se_instancia_correctamente():
    mazo_ = Mazo()
    assert mazo_ != None

def test_2_entre_dos_mazos_no_hay_repetidos():
    mazo_ = Mazo()
    for _ in range(ITERACIONES_MANOS):
        mano1, mano2 = mazo_.mezclar_y_repartir()
        set1 = set(mano1)
        set2 = set(mano2)
        assert set1 - set2 == set1
        assert set2 - set1 == set2

def main_test_mazo():
    print("Corriendo tests de mazo...")
    test_1_mazo_se_instancia_correctamente()
    test_2_entre_dos_mazos_no_hay_repetidos()
    print("Todos los tests de mazo pasaron exitosamente!")

if __name__ == '__main__':
    main_test_mazo()
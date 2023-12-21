import sys
sys.path.append('../')

from cartas import *
from flor import *

from src.jugador import Jugador

def test_1_gana_el_jugador_con_la_suma_tantos_mas_alta():
    j1 = Jugador('1')
    j2 = Jugador('2')
    
    c11 = Seis("6_bas.png")
    c12 = Cinco("5_bas.png")
    c13 = Cuatro("4_bas.png")
    
    c21 = Dos("2_copa.png")
    c22 = Tres("3_copa.png")
    c23 = Cuatro("4_copa.png")
    
    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])
    
    flor = Flor(j1, j2)
    resultado = flor.aceptar_flor()
    
    assert(resultado.puntos_ganador == 35)
    assert(resultado.puntos_perdedor == 29)
    assert(resultado.puntos_a_sumar == 4)
    assert(resultado.ganador == j1)
    assert(resultado.perdedor == j2)
    
def test_2_si_un_jugador_no_tiene_3_cartas_del_mismo_palo_suma_0():
    j1 = Jugador('1')
    j2 = Jugador('2')
    
    c11 = Seis("6_esp.png")
    c12 = Cinco("5_bas.png")
    c13 = Cuatro("4_bas.png")
    
    c21 = Dos("2_oro.png")
    c22 = Tres("3_esp.png")
    c23 = Cuatro("4_copa.png")
    
    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])
    
    flor = Flor(j1, j2)
    resultado = flor.aceptar_flor()
    
    assert(resultado.puntos_ganador == 0)
    assert(resultado.puntos_perdedor == 0)
    assert(resultado.puntos_a_sumar == 4)
    assert(resultado.ganador == None)
    assert(resultado.perdedor == None)

def test_3_si_se_rechaza_una_flor_se_gana_3_puntos(): 
    j1 = Jugador('1')
    j2 = Jugador('2')

    flor = Flor(j1, j2)
    puntos_a_sumar = flor.rechazar_flor() 
    puntos_esperados_a_sumar = 3 
    
    assert(puntos_a_sumar == puntos_esperados_a_sumar)

def test_4_contraflor(): 
    j1 = Jugador('1')
    j2 = Jugador('2')
    
    c11 = Seis("6_bas.png")
    c12 = Cinco("5_bas.png")
    c13 = Cuatro("4_bas.png")
    
    c21 = Dos("2_copa.png")
    c22 = Tres("3_copa.png")
    c23 = Cuatro("4_copa.png")
    
    j1.recibir_cartas([c11, c12, c13])
    j2.recibir_cartas([c21, c22, c23])
    
    flor = Flor(j1, j2)
    flor.contraflor()
    resultado = flor.aceptar_flor()
    
    assert(resultado.puntos_ganador == 35)
    assert(resultado.puntos_perdedor == 29)
    assert(resultado.puntos_a_sumar == 6)
    assert(resultado.ganador == j1)
    assert(resultado.perdedor == j2)
    
    puntos_a_sumar = flor.rechazar_flor() 
    puntos_esperados_a_sumar = 4 
    
    assert(puntos_a_sumar == puntos_esperados_a_sumar)
    assert("Contra Flor" == flor.obtener_fase())

def main():
    print("Corriendo tests de flor...")
    test_1_gana_el_jugador_con_la_suma_tantos_mas_alta()
    test_2_si_un_jugador_no_tiene_3_cartas_del_mismo_palo_suma_0()
    test_3_si_se_rechaza_una_flor_se_gana_3_puntos()
    test_4_contraflor()
    print("Todos los tests de flor pasan exitosamente!")

if __name__ == '__main__':
    main()
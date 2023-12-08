#from cartas import _Carta
from jugador import Jugador

from math import floor

FASES_Y_PUNTOS = {
    "FALTAENVIDO": 0,
    "ENVIDO": 2,
    "REALENVIDO": 3,
    "ENVIDO_ENVIDO": 4,
    "ENVIDO_REALENVIDO": 5,
    "ENVIDO_ENVIDO_REALENVIDO": 7,
}


class ResultadoEnvido:
    def __init__(self, ganador, tantos_ganador, perdedor, tantos_perdedor, puntos_a_sumar):
        self.ganador = ganador
        self.puntos_ganador = tantos_ganador
        self.perdedor = perdedor
        self.puntos_perdedor = tantos_perdedor
        self.puntos_a_sumar = puntos_a_sumar

class Envido:
    """Clase que representa el envido de una partida de truco"""
    def __init__(self, jugador_canto: "Jugador", jugador_oponente: "Jugador", fase: str, max_puntos: int) -> None:
        self.jugador_canto = jugador_canto
        self.jugador_oponente = jugador_oponente
        self.max_puntos = max_puntos
        self.fase = fase

        if fase == "FALTAENVIDO":
            self.es_falta_envido = True
        else:
            self.es_falta_envido = False

    def calcular_tantos(self, cartas_jugador: list) -> int:
        envido_maximo = 0
        for carta in cartas_jugador:
            for carta2 in cartas_jugador:
                envido = 0
                if carta != carta2:
                    if carta.palo == carta2.palo:
                        if carta.valor < 10 and carta2.valor < 10:
                            envido = carta.valor + carta2.valor + 20
                        elif carta.valor < 10 and carta2.valor >= 10:
                            envido = carta.valor + 20
                        else:
                            envido = 20
                        if envido > envido_maximo:
                            envido_maximo = envido
                    elif carta.valor > envido_maximo and carta.valor < 10:
                        envido_maximo = carta.valor 
        
        return envido_maximo
        
    def comparar_tantos(self):
        cartas_jugador_canto = self.jugador_canto.obtener_cartas()
        cartas_jugador_oponente = self.jugador_oponente.obtener_cartas()
        tantos_jugador_canto = self.calcular_tantos(cartas_jugador_canto)
        tantos_jugador_oponente = self.calcular_tantos(cartas_jugador_oponente)

        if tantos_jugador_canto > tantos_jugador_oponente:
            return ResultadoEnvido(self.jugador_canto, tantos_jugador_canto, self.jugador_oponente, tantos_jugador_oponente, FASES_Y_PUNTOS[self.fase])
        elif tantos_jugador_canto < tantos_jugador_oponente:
            return ResultadoEnvido(self.jugador_oponente, tantos_jugador_oponente, self.jugador_canto, tantos_jugador_canto, FASES_Y_PUNTOS[self.fase])
        else:
            return ResultadoEnvido(None, tantos_jugador_canto, None, tantos_jugador_oponente, FASES_Y_PUNTOS[self.fase])

    def aceptar_envido(self):
        res_envido = self.comparar_tantos()
        if self.es_falta_envido:
            if res_envido.ganador == None:
                res_envido.puntos_a_sumar = None
            else:
                res_envido.puntos_a_sumar = self.max_puntos - res_envido.perdedor.obtener_puntos()
        return res_envido

    
    def rechazar_envido(self):
        if self.es_falta_envido:
            return FASES_Y_PUNTOS[self.fase] + 1

        return floor(FASES_Y_PUNTOS[self.fase] / 2)
        

    def _actualizar(self, fase_nueva=None):
        if fase_nueva:
            self.fase = fase_nueva

        aux = self.jugador_canto
        self.jugador_canto = self.jugador_oponente
        self.jugador_oponente = aux

    def actualizar(self, tipo_envido):
        if tipo_envido == "FALTAENVIDO":
            if self.es_falta_envido:
                return False
            self._actualizar()
            return True

        fase_nueva = self.fase + "_" + tipo_envido
        if fase_nueva in FASES_Y_PUNTOS:
            self._actualizar(fase_nueva)
            return True
        
        return False
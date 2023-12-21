from enum import Enum
from jugador import Jugador

FLOR = "FLOR"
CONTRAFLOR = "CONTRAFLOR"

class Fase(Enum):
    """
    Enum que representa las diferentes fases de flor. 
    """
    FLOR = {
        "fase": "Flor",
        "puntos_ganador": 4,
        "puntos_rechazar": 3
    }
    CONTRAFLOR = {
        "fase": "Contra Flor",
        "puntos_ganador": 6,
        "puntos_rechazar": 4
    }


class ResultadoFlor:
    """
    Clase que representa el resultado de una flor para que despues se pueda
    ver con mas facilidad quien gano y quien perdio, y cuantos puntos se suman

    Atributos:

    * `ganador`: Jugador que gano la flor
    * `puntos_ganador`: Puntos que tiene el ganador
    * `perdedor`: Jugador que perdio la flor
    * `puntos_perdedor`: Puntos que tiene el perdedor
    * `puntos_a_sumar`: Puntos que se suman al ganador
    """
    def __init__(self, ganador: Jugador, tantos_ganador: int, perdedor: Jugador, tantos_perdedor: int, puntos_a_sumar: int) -> None:
        """
        Inicializa el resultado de flor

        Recibe:

        * `ganador`: Jugador que gano la flor 
        * `tantos_ganador`: Puntos que tiene el ganador
        * `perdedor`: Jugador que perdio la flor
        * `tantos_perdedor`: Puntos que tiene el perdedor
        * `puntos_a_sumar`: Puntos que se suman al ganador
        """
        self.ganador = ganador
        self.puntos_ganador = tantos_ganador
        self.perdedor = perdedor
        self.puntos_perdedor = tantos_perdedor
        self.puntos_a_sumar = puntos_a_sumar


class Flor: 
    """
    Clase que representa un canto de Flor de una partida de truco
    
    Atributos:

    * `jugador_canto`: Jugador que canto el envido
    * `jugador_oponente`: Jugador que tiene que responder el envido
    """
    def __init__(self, jugador_canto: Jugador, jugador_oponente: Jugador) -> None:
        """
        Inicializa la flor. 
        """
        self.jugador_canto = jugador_canto
        self.jugador_oponente = jugador_oponente
        self.fase = Fase[FLOR]
    
    def _no_tiene_3_cartas_del_mismo_palo(self, jugador: Jugador):
        """
        Hace una verificacion de que si el jugador no tiene 3 cartas iguales
        
        Pre: 
        * Jugador tiene que tener 3 cartas 
        
        Post: 
        * Devuelve true si no se cumple la condicion. False cosa contrario  
        """
        cartas = jugador.obtener_cartas()
        return not (cartas[0].palo == cartas[1].palo == cartas[2].palo)
    
    def _calcular_tantos(self, jugador: Jugador): 
        """
        Suma los tantos de un jugador para la flor 
        
        Pre:
        * Jugador tiene que tener 3 cartas 
        
        Post: 
        * Devuelve los tantos  del jugador. En caso de no tener 3 cartas 
        iguales devuelve 0 
        
        """
        if self._no_tiene_3_cartas_del_mismo_palo(jugador): 
            return 0 
        
        tantos = 20 
        for carta in jugador.obtener_cartas():
            if carta.numero < 10: 
                tantos += carta.numero
        
        return tantos
        
    def aceptar_flor(self) -> ResultadoFlor:
        """
        Acepta la flor. Compara los tantos de cada jugador y devuelve 
        una instancia de resultado con los pertinentes datos 
        """
        tantos_jugador_canto = self._calcular_tantos(self.jugador_canto)
        tantos_jugador_oponente = self._calcular_tantos(self.jugador_oponente)
        
        if tantos_jugador_canto > tantos_jugador_oponente:
            return ResultadoFlor(self.jugador_canto, tantos_jugador_canto, self.jugador_oponente, tantos_jugador_oponente, self.fase.value["puntos_ganador"])
        elif tantos_jugador_canto < tantos_jugador_oponente:
            return ResultadoFlor(self.jugador_oponente, tantos_jugador_oponente, self.jugador_canto, tantos_jugador_canto, self.fase.value["puntos_ganador"])
        else:
            return ResultadoFlor(None, tantos_jugador_canto, None, tantos_jugador_oponente, self.fase.value["puntos_ganador"])

    def rechazar_flor(self) -> int: 
        """
        Rechaza la flor y devuele el puntaje a sumar para el jugador
        que le rechazaron la flor 
        """
        return self.fase.value["puntos_rechazar"]
    
    def contraflor(self): 
        """
        Canta la contraflor, cambiando la fase de la flor a contraflor
        """
        self.fase = Fase[CONTRAFLOR]
        self.jugador_canto, self.jugador_oponente = self.jugador_oponente, self.jugador_canto
    
    def obtener_fase(self): 
        """
        Devuelve la fase actual de la flor
        """
        return self.fase.value["fase"]
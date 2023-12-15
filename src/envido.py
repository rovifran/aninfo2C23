from jugador import Jugador

from math import floor

FALTAENVIDO = "FALTAENVIDO"

FASES_Y_PUNTOS = {
    "FALTAENVIDO": 0,
    "ENVIDO": 2,
    "REALENVIDO": 3,
    "ENVIDO_ENVIDO": 4,
    "ENVIDO_REALENVIDO": 5,
    "ENVIDO_ENVIDO_REALENVIDO": 7,
}


class ResultadoEnvido:
    """
    Clase que representa el resultado de un envido para que despues se pueda
    ver con mas facilidad quien gano y quien perdio, y cuantos puntos se suman

    Atributos:

    * `ganador`: Jugador que gano el envido
    * `puntos_ganador`: Puntos que tiene el ganador
    * `perdedor`: Jugador que perdio el envido
    * `puntos_perdedor`: Puntos que tiene el perdedor
    * `puntos_a_sumar`: Puntos que se suman al ganador
    """
    def __init__(self, ganador: Jugador, tantos_ganador: int, perdedor: Jugador, tantos_perdedor: int, puntos_a_sumar: int) -> None:
        """
        Inicializa el resultado del envido

        Recibe:

        * `ganador`: Jugador que gano el envido
        * `tantos_ganador`: Puntos que tiene el ganador
        * `perdedor`: Jugador que perdio el envido
        * `tantos_perdedor`: Puntos que tiene el perdedor
        * `puntos_a_sumar`: Puntos que se suman al ganador
        """
        self.ganador = ganador
        self.puntos_ganador = tantos_ganador
        self.perdedor = perdedor
        self.puntos_perdedor = tantos_perdedor
        self.puntos_a_sumar = puntos_a_sumar

    def __str__(self) -> str:
        """
        Devuelve una representacion en string del resultado del envido
        """
        return f"Ganador: {self.ganador}, Puntos Ganador: {self.puntos_ganador}, Perdedor: {self.perdedor}, Puntos Perdedor: {self.puntos_perdedor}, Puntos a sumar: {self.puntos_a_sumar}"
    
    def __repr__(self) -> str:
        """
        Tiene el mismo comportamiento que al llamar a str(envido), esta implementado
        para las distintas estructuras que usan repr en vez de str
        """
        return str(self)

class Envido:
    """
    Clase que representa un canto de Envido de una partida de truco
    
    Atributos:

    * `jugador_canto`: Jugador que canto el envido
    * `jugador_oponente`: Jugador que tiene que responder el envido
    * `fase`: Fase del envido que se esta jugando
    * `max_puntos`: Puntos a los que se juega
    """
    def __init__(self, jugador_canto: Jugador, jugador_oponente: Jugador, fase: str, max_puntos: int) -> None:
        """
        Inicializa el envido
        """
        self.jugador_canto = jugador_canto
        self.jugador_oponente = jugador_oponente
        self.max_puntos = max_puntos
        self.fase = fase

        if fase == FALTAENVIDO:
            self.es_falta_envido = True
        else:
            self.es_falta_envido = False

    def _calcular_tantos(self, cartas_jugador: list) -> int:
        """
        Recibe las cartas de un jugador y devuelve los tantos que tiene
        segun la mano. Las distintas combinaciones para los tantos segun
        las cartas son contempladas y se devuelve aquella que de mas puntos

        Precondiciones:
        
        * `cartas_jugador` es una lista de 3 cartas
        * Esta funcion se llama solo cuando se juega un envido con sus campos correspondientes

        Postcondiciones:

        * Devuelve los tantos que suma la mano
        """
        envido_maximo = 0
        for carta in cartas_jugador:
            for carta2 in cartas_jugador:
                envido = 0
                if carta != carta2:
                    if carta.palo == carta2.palo:
                        if carta.numero < 10 and carta2.numero < 10:
                            envido = carta.numero + carta2.numero + 20
                        elif carta.numero < 10 and carta2.numero >= 10:
                            envido = carta.numero + 20
                        else:
                            envido = 20
                        if envido > envido_maximo:
                            envido_maximo = envido
                    elif carta.numero > envido_maximo and carta.numero < 10:
                        envido_maximo = carta.numero 
        
        return envido_maximo
        
    def _comparar_tantos(self) -> ResultadoEnvido:
        """
        Se encarga de comparar los tantos de los jugadores y devuelve el resultado del envido.
        Si ambos jugadores tienen la misma cantidad de tantos, devuelve un resultado de empate, 
        esto es, con ambos jugadores como None, y deja que la logica del juego decida quien gano
        en base al jugador que es mano

        Precondiciones:

        * Se llama solo cuando se juega un envido con sus campos correspondientes
        * Se llama solo cuando se termina de jugar el envido

        Postcondiciones:

        * Devuelve una instancia de ResultadoEnvido con el ganador, el perdedor, los tantos
        de cada uno y los puntos a sumar
        """
        cartas_jugador_canto = self.jugador_canto.obtener_cartas()
        cartas_jugador_oponente = self.jugador_oponente.obtener_cartas()
        tantos_jugador_canto = self._calcular_tantos(cartas_jugador_canto)
        tantos_jugador_oponente = self._calcular_tantos(cartas_jugador_oponente)

        if tantos_jugador_canto > tantos_jugador_oponente:
            return ResultadoEnvido(self.jugador_canto, tantos_jugador_canto, self.jugador_oponente, tantos_jugador_oponente, FASES_Y_PUNTOS[self.fase])
        elif tantos_jugador_canto < tantos_jugador_oponente:
            return ResultadoEnvido(self.jugador_oponente, tantos_jugador_oponente, self.jugador_canto, tantos_jugador_canto, FASES_Y_PUNTOS[self.fase])
        else:
            return ResultadoEnvido(None, tantos_jugador_canto, None, tantos_jugador_oponente, FASES_Y_PUNTOS[self.fase])

    def aceptar_envido(self) -> ResultadoEnvido:
        """
        Se encarga de aceptar el envido y devuelve el resultado del envido, que es una
        instancia de ResultadoEnvido. Se encarga de manejar los casos especiales de
        falta envido, donde se tiene que devolver el resultado con los puntos a sumar
        correspondientes

        Precondiciones:

        * Se llama solo cuando se juega un envido con sus campos correspondientes

        Postcondiciones:

        * Devuelve una instancia de ResultadoEnvido con el ganador, el perdedor, los tantos
        de cada uno y los puntos a sumar
        """
        res_envido = self._comparar_tantos()
        if self.es_falta_envido:
            if res_envido.ganador == None:
                res_envido.puntos_a_sumar = None
            else:
                res_envido.puntos_a_sumar = self.max_puntos - res_envido.perdedor.obtener_puntos()
        return res_envido

    
    def rechazar_envido(self) -> int:
        """
        Se encarga de rechazar el envido, en cuyo caso devuelve la cantidad de puntos que se
        suman al jugador contrincante al que rechazo. Contempla los casos especiales de Falta Envido

        Precondiciones:

        * Se llama solo cuando se juega un envido con sus campos correspondientes

        Postcondiciones:

        * Devuelve la cantidad de puntos a sumarse 
        """
        if self.es_falta_envido:
            return FASES_Y_PUNTOS[self.fase] + 1

        return floor(FASES_Y_PUNTOS[self.fase] / 2)
        

    def _actualizar(self, fase_nueva: str = None) -> None:
        """
        Se encarga de actualizar la fase y cambiar quien canto el envido y quien tiene que responderlo

        Precondiciones:

        * `fase_nueva` es una fase valida del envido, y en caso de cantarse Falta Envido es None
        (porque es una forma de calcular los puntos a sumar si no se quiere el envido)

        Postcondiciones:

        * Se actualiza la fase del envido
        * Se cambia el jugador que canto el envido por el que tiene que responderlo y viceversa
        """
        if fase_nueva:
            self.fase = fase_nueva

        aux = self.jugador_canto
        self.jugador_canto = self.jugador_oponente
        self.jugador_oponente = aux

    def actualizar(self, tipo_envido: str) -> bool:
        """
        Se encarga de actualizar el envido, en caso de que se cante un envido valido, 
        y devuelve True o False en caso de que se haya actualizado correctamente o no.
        Contempla el caso especial de cantar el Falta Envido en cualquier instancia

        Precondiciones:

        * `tipo_envido` es una fase valida del envido

        Postcondiciones:

        * Devuelve True si se actualizo correctamente, False en caso contrario
        """
        if tipo_envido == FALTAENVIDO:
            if self.es_falta_envido:
                return False
            self._actualizar()
            self.es_falta_envido = True
            return True

        fase_nueva = self.fase + "_" + tipo_envido
        if fase_nueva in FASES_Y_PUNTOS:
            self._actualizar(fase_nueva)
            return True
        
        return False
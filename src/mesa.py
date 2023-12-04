#import jugador

class Mesa:
    """
    Clase que representa la mesa de juego del Truco Argentino.
    Recibe las cartas de cada jugador, las compara y devuelve el ganador de esta mano.
    Al finalizar la mano, se le suman los puntos al ganador.

    Atributos:
        mano: Es una lista que contiene las cartas de cada jugador en la mesa
        
    """

    def __init__(self):
        self.mano_actual = []
        self.jugadores = []
        self.cartas_jugadas = []
        self.ganador = None
        

    def recibirCarta(self, carta, jugador):
        """
        Recibe la carta jugada por el jugador y la agrega a la mesa.

        Precondiciones:
            - carta es una instancia de la clase Carta
            - jugador es una instancia de la clase Jugador
            - Se reciben 2 cartas por mano, una por cada jugador
        PostCondiciones:
            - Se agrega la carta a la mesa
            - Si es la segunda carta jugada en la mano, se compara y se guarda quien gana cada mano
        """

        """"
        mano.append(carta)
        if len(mano) == 2:
            self.compararCartas()
            asignar punto a ganador
            self.mano = []
        """

        """
        [][][]
        [][][]
        1 0 1
        """
        self.mano_actual.append((carta, jugador))
        if len(self.mano_actual) == 2:
            self.ganador = self.compararCartas()
            self.mano_actual = []
            

        self.cartas_jugadas.append(carta)


    def compararCartas(self):
        """
        Compara las cartas de la mesa y devuelve el ganador de la mano.

        Precondiciones:
            - Se reciben 2 cartas por mano, una por cada jugador
        PostCondiciones:
            - Se devuelve el ganador de la mano
        """
        carta1, jugador1 = self.mano_actual[0]
        carta2, jugador2 = self.mano_actual[1]
        
        if carta1 > carta2:
            return jugador1
        if carta1 < carta2:
            return jugador2
        return None

    def getGanador(self):
        """
        Devuelve el ganador de la mano.

        Precondiciones:
            - Se reciben 2 cartas por mano, una por cada jugador
        PostCondiciones:
            - Se devuelve el ganador de la mano
        """
        return self.ganador
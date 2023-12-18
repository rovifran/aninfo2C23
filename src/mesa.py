
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
        self.cartas_jugadas = [[]]
        self.ganador_mano = None
        
 
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


        [[c1,c2][c4,c3][]] #las sublistas estarian ordenadas para graficar arriba la mas grande
        """
        
        if len(self.mano_actual) > 0:
            self.mano_actual.append((carta, jugador))
            self.ganador_mano = self.compararCartas()
            self.cartas_jugadas.append([])
            self.mano_actual = []
            return

        for mano in self.cartas_jugadas:
            if len(mano) == 0:
                mano.append((carta, jugador))
                self.mano_actual = mano
                break

    def manoActualEstaCompleta(self):
        """
        Devuelve True si la mano actual esta completa, False en caso contrario.
        Como la mano actual se resetea cada vez que hay 2 cartas en la mesa, una
        forma de ver si esta completa la mano, es ver si la mano actual tiene 0 cartas
        siempre que se llame este metodo despues de tirar una carta, nunca antes.
        
        Precondiciones:
            - Se reciben 2 cartas por mano, una por cada jugador
        PostCondiciones:
            - Se devuelve True si la mano esta completa, False en caso contrario
        """
        return len(self.mano_actual) == 0

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
            self.mano_actual[0], self.mano_actual[1] = self.mano_actual[1], self.mano_actual[0]
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
        return self.ganador_mano
    


    
import mazo 
import cartas
import mesa
import random
#import jugador

class Partida:
    def __init__(self, j1, j2, max_puntos, flor) -> None:
        self.jugador_1 = j1
        self.jugador_2 = j2
        self.jugador_actual = None
        self.ganador = None
        self.max_puntos = max_puntos
        self.flor = flor
        self.mazo = mazo.Mazo()
        self.mesa = mesa.Mesa()


    def jugar_mano(self):

        self.mesa.recibirCarta(self.jugador_actual.jugar_carta)

    def iniciar_mano(self):
        if self.jugador_actual == None:
            self.jugador_actual = random.choice([self.jugador_1, self.jugador_2])
        else:
            self.jugador_actual = self.jugador_1 if self.jugador_actual == self.jugador_2 else self.jugador_2

        self.mazo.mezclar()
        mano_j1, mano_j2 = self.mazo.repartir()
        self.jugador_1.recibir_mano(mano_j1)
        self.jugador_2.recibir_mano(mano_j2)


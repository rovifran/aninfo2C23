import mazo 
import mesa
#import jugador

PUNTOS_RONDA_SIMPLE = 1

class Partida:
    """
    Clase que representa una partida de truco

    Esta clase se encarga de manejar la logica del juego, como por ejemplo:
    * Iniciar una mano, mezclando el mazo y repartiendo las cartas
    * Cambiar el turno de los jugadores despues de tirar una carta
    * Determinar el ganador de una ronda
    """
    def __init__(self, j1, j2, max_puntos, flor, mesa) -> None:
        """
        Inicializa la partida de truco, recibiendo:

        * El jugador 1, que va a empezar la partida siendo mano
        * El jugador 2
        * La cantidad de puntos a jugar
        * Si se juega con flor o sin flor
        * La mesa donde se van a tirar las cartas

        Inicializa el mazo para jugar
        """
        self.jugador_actual = j1
        self.jugador_contrario = j2
        self.jugador_mano = j2 # para ver cosas como quien gano en el envido si empatan, o si se empardan las 3 manos
        self.ganador_por_mano = []
        self.ganador_final_mano = None
        self.max_puntos = max_puntos
        self.flor = flor
        self.mazo = mazo.Mazo()
        self.mesa = mesa

    def cambiar_turno(self):
        self.jugador_actual, self.jugador_contrario = self.jugador_contrario, self.jugador_actual

    def jugar_carta(self, carta):

        self.mesa.recibirCarta(self.jugador_actual.jugar_carta(carta))

        if not self.mesa.manoActualEstaCompleta():
            self.cambiar_turno()
        
        else:
            ganador_mano = self.mesa.getGanador()
            self.ganador_por_mano.append(ganador_mano)
            if ganador_mano != None and ganador_mano != self.jugador_actual:
                self.cambiar_turno()

    def iniciar_mano(self):
        self.jugador_mano = self.jugador_actual if self.jugador_mano == self.jugador_contrario else self.jugador_contrario

        self.jugador_actual = self.jugador_mano
        self.jugador_contrario = self.jugador_actual if self.jugador_mano == self.jugador_contrario else self.jugador_contrario

        self.mazo.mezclar()
        mano_j1, mano_j2 = self.mazo.repartir()
        self.jugador_actual.recibir_mano(mano_j1)
        self.jugador_contrario.recibir_mano(mano_j2)
    
    def ronda_esta_terminada(self):
        return self.ganador_final_mano != None 
    
    def sumar_puntos_a_ganador(self):
        if not self.ronda_esta_terminada():
            return
        self.ganador_final_mano.sumar_puntos(PUNTOS_RONDA_SIMPLE)

    def definir_ganador(self):

        def _triple_parda():
            return len(self.ganador_por_mano) == 3 and not self.jugador_actual in self.ganador_por_mano and not self.jugador_contrario in self.ganador_por_mano

        def _mismo_ganador_primeras_dos_manos():
            return self.ganador_por_mano[0] == self.ganador_por_mano[1]

        def _ganador_en_tercera_mano_por_todo_parda():
            return self.ganador_por_mano[0] == None and self.ganador_por_mano[1] == None and self.ganador_por_mano[2] != None
        
        def _parda_solo_en_primera_mano():
            return self.ganador_por_mano[0] == None and self.ganador_por_mano[1] != None
            
        def _ganador_en_tercera_mano_sin_parda():
            return self.ganador_por_mano[0] != None and self.ganador_por_mano[1] != None and self.ganador_por_mano[2] != None
        
        def _ganador_en_tercera_mano_por_parda():
            return self.ganador_por_mano[0] != None and self.ganador_por_mano[1] != None and self.ganador_por_mano[0] != self.ganador_por_mano[1]  and self.ganador_por_mano[2] == None
        
        if len(self.ganador_por_mano) < 1:
            return

        if _parda_solo_en_primera_mano():
            self.ganador_final_mano = self.ganador_por_mano[1]
            return    

        if _mismo_ganador_primeras_dos_manos():
            self.ganador_final_mano = self.ganador_por_mano[0]
            return
        
        if _triple_parda():
            self.ganador_final_mano = self.jugador_mano
            return    
            
        if _ganador_en_tercera_mano_por_todo_parda() or _ganador_en_tercera_mano_sin_parda(): 
            self.ganador_final_mano = self.ganador_por_mano[2]
            return
        
        if _ganador_en_tercera_mano_por_parda():
            self.ganador_final_mano = self.ganador_por_mano[0]


import mazo 
import envido as env
import cantar_truco as truco
from mesa import Mesa
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
    def __init__(self, j1, j2, max_puntos, flor, mesa: Mesa) -> None:
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
        self.jugador_canto_envido = None
        self.ganador_por_mano = []
        self.envido_actual = None
        self.truco_actual = None
        self.ganador_final_mano = None
        self.max_puntos = max_puntos
        self.flor = flor
        self.mazo = mazo.Mazo()
        self.mesa = mesa

    def cambiar_turno(self):
        self.jugador_actual, self.jugador_contrario = self.jugador_contrario, self.jugador_actual

    def obtener_jugador_actual(self):
        return self.jugador_actual

    def obtener_jugador_contrario(self):
        return self.jugador_contrario
    
    def jugar_carta(self, carta):

        self.mesa.recibirCarta(self.jugador_actual.jugar_carta(carta), self.jugador_actual)

        if not self.mesa.manoActualEstaCompleta():
            self.cambiar_turno()
        
        else:
            ganador_mano = self.mesa.getGanador()
            self.ganador_por_mano.append(ganador_mano)
            if ganador_mano != None and ganador_mano != self.jugador_actual:
                self.cambiar_turno()

    def cantar_envido(self, tipo_envido):
        if self.jugador_canto_envido == None:
            self.jugador_canto_envido = self.jugador_actual
            self.envido_actual = env.Envido(self.jugador_actual, self.jugador_contrario, tipo_envido, self.max_puntos)
            self.cambiar_turno()

        else:
            if self.envido_actual.actualizar(tipo_envido):
                self.cambiar_turno()

    def _resetear_envido(self):
        if self.jugador_actual != self.jugador_canto_envido:
            self.cambiar_turno()

        self.envido_actual = None
        self.jugador_canto_envido = None        

    def aceptar_envido(self):
        res_envido = self.envido_actual.aceptar_envido()        
        if res_envido.ganador == None:
            if res_envido.puntos_a_sumar == None:
                contrincante = self.jugador_contrario if self.jugador_mano == self.jugador_actual else self.jugador_actual
                self.jugador_mano.sumar_puntos(self.max_puntos - contrincante.obtener_puntos())
            else:
                self.jugador_mano.sumar_puntos(res_envido.puntos_a_sumar)
        else: 
            res_envido.ganador.sumar_puntos(res_envido.puntos_a_sumar)

        self._resetear_envido()

        return res_envido

    def rechazar_envido(self):
        puntos = self.envido_actual.rechazar_envido()
        self.jugador_contrario.sumar_puntos(puntos)

    def cantar_truco(self, tipo_truco):
        if self.truco_actual == None:
            self.truco_actual = truco.Truco(tipo_truco)
            self.cambiar_turno()

        else:
            self.truco_actual.actualizar(tipo_truco)
            self.cambiar_turno()

    def aceptar_truco(self):
        self.truco_actual.aceptar_truco()
        self.cambiar_turno()

    def _resetear_truco(self):
        self.truco_actual = None

    def rechazar_truco(self):
        puntos = self.truco_actual.rechazar_truco()
        self.jugador_contrario.sumar_puntos(puntos)
        self.cambiar_turno()


    def iniciar_mano(self):
        jugador_actual = self.jugador_actual
        jugador_contrario = self.jugador_contrario

        if self.jugador_mano == jugador_actual:
            self.jugador_mano = jugador_contrario
            self.cambiar_turno()
        else:
            self.jugador_mano = jugador_actual

        self.ganador_por_mano = []
        self.ganador_final_mano = None
        self.jugador_canto_envido = None

        self.mazo.mezclar()
        mano_j1, mano_j2 = self.mazo.repartir()
        self.jugador_actual.recibir_cartas(mano_j1)
        self.jugador_contrario.recibir_cartas(mano_j2)

    
    def ronda_esta_terminada(self):
        return self.ganador_final_mano != None 
    
    
    def sumar_puntos_a_ganador(self):
        if not self.ronda_esta_terminada():
            return
        
        if self.truco_actual and self.truco_actual.fue_aceptado():
            puntos = self.truco_actual.calcular_puntos()
            self.ganador_final_mano.sumar_puntos(puntos)
            self._resetear_truco()
            return

        self.ganador_final_mano.sumar_puntos(PUNTOS_RONDA_SIMPLE)


    def hay_ganador_ronda(self):
        self.definir_ganador()
        return self.ganador_final_mano != None

    def definir_ganador(self):
        def _triple_parda():
            return len(self.ganador_por_mano) == 3 and not self.jugador_actual in self.ganador_por_mano and not self.jugador_contrario in self.ganador_por_mano

        def _mismo_ganador_primeras_dos_manos():
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] == self.ganador_por_mano[1]

        def _parda_solo_en_segunda_mano():
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] != None and self.ganador_por_mano[1] == None

        def _ganador_en_tercera_mano_por_todo_parda():
            return len(self.ganador_por_mano) == 3 and self.ganador_por_mano[0] == None and self.ganador_por_mano[1] == None and self.ganador_por_mano[2] != None
        
        def _parda_solo_en_primera_mano():
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] == None and self.ganador_por_mano[1] != None
            
        def _ganador_en_tercera_mano_sin_parda():
            return len(self.ganador_por_mano) == 3 and self.ganador_por_mano[0] != None and self.ganador_por_mano[1] != None and self.ganador_por_mano[2] != None
        
        def _ganador_en_tercera_mano_por_parda():
            return len(self.ganador_por_mano) == 3 and self.ganador_por_mano[0] != None and self.ganador_por_mano[1] != None and self.ganador_por_mano[0] != self.ganador_por_mano[1]  and self.ganador_por_mano[2] == None
        
        if len(self.ganador_por_mano) <= 1:
            return

        if _parda_solo_en_primera_mano():
            self.ganador_final_mano = self.ganador_por_mano[1]
            return
          
        if _triple_parda():
            self.ganador_final_mano = self.jugador_mano
            return    
                 
        if _parda_solo_en_segunda_mano():
            self.ganador_final_mano = self.ganador_por_mano[0]
            return
        
        if _mismo_ganador_primeras_dos_manos():
            self.ganador_final_mano = self.ganador_por_mano[0]
            return
        
        if _ganador_en_tercera_mano_por_todo_parda() or _ganador_en_tercera_mano_sin_parda(): 
            self.ganador_final_mano = self.ganador_por_mano[2]
            return
        
        if _ganador_en_tercera_mano_por_parda():
            self.ganador_final_mano = self.ganador_por_mano[0]
            return
        


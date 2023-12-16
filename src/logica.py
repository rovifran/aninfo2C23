import mazo 
import envido as env
import cantar_truco as truco
from mesa import Mesa
from jugador import Jugador

PUNTOS_RONDA_SIMPLE = 1

class Partida:
    """
    Clase que representa una partida de truco

    Esta clase se encarga de manejar la logica del juego, como por ejemplo:
    * Iniciar una mano, mezclando el mazo y repartiendo las cartas
    * Cambiar el turno de los jugadores despues de tirar una carta
    * Determinar el ganador de una ronda
    """
    def __init__(self, j1: Jugador, j2: Jugador, max_puntos: int, mesa: Mesa) -> None:
        """
        Inicializa la partida de truco, recibiendo:

        * El jugador 1, que va a empezar la partida siendo mano
        * El jugador 2
        * La cantidad de puntos a jugar
        * La mesa donde se van a tirar las cartas

        Atributos:

        * jugador_actual: Jugador que tiene el turno actual
        * jugador_contrario: Jugador que no tiene el turno actual
        * jugador_mano: Jugador que es mano en la ronda actual
        * jugador_canto_envido: Jugador que canto el envido
        * ganador_por_mano: Lista de jugadores que ganaron cada mano
        * envido_actual: Objeto que representa el envido actual
        * truco_actual: Objeto que representa el truco actual
        * ganador_final_mano: Jugador que gano la ronda
        * max_puntos: Cantidad de puntos a jugar
        * mazo: Mazo de cartas
        * mesa: Mesa donde se juega la partida

        A la hora de inicializarse, tambien inicializa el mazo para jugar (poruqe
        es el unico lugar en donde se usa)
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
        self.mazo = mazo.Mazo()
        self.mesa = mesa

    def cambiar_turno(self) -> None:
        """
        Cambia el turno de los jugadores, es decir, el jugador que tiene el turno
        pasa a ser el jugador contrario, y viceversa

        Precondiciones:

        * Los jugadores son instancias de la clase `Jugador`

        Postcondiciones:

        * El jugador actual es el jugador contrario
        * El jugador contrario es el jugador actual
        """

        self.jugador_actual, self.jugador_contrario = self.jugador_contrario, self.jugador_actual

    def obtener_jugador_actual(self) -> Jugador:
        """
        Devuelve el jugador que tiene el turno actual
        """

        return self.jugador_actual

    def obtener_jugador_contrario(self) -> Jugador:
        """
        Devuelve el jugador que no tiene el turno actual
        """
        
        return self.jugador_contrario
    
    def jugar_carta(self, carta: "Carta") -> None:
        """
        Hace que el jugador actual juegue una carta, y la mesa la reciba.
        Se encarga de cambiar el turno del que tira la carta si la mano no esta completa,
        y segun quien gano la mano, cambia el turno del jugador mano.

        Precondiciones:

        * La carta es una instancia de la clase `Carta`
        * La mesa es una instancia de la clase `Mesa`

        Postcondiciones:

        * La mesa recibe la carta jugada por el jugador actual
        * Si la mano no esta completa, cambia el turno del jugador actual
        * Si la mano esta completa, verifica quien gano la mano para cambiar el turno o no
        """

        self.mesa.recibirCarta(self.jugador_actual.jugar_carta(carta), self.jugador_actual)

        if not self.mesa.manoActualEstaCompleta():
            self.cambiar_turno()
        
        else:
            ganador_mano = self.mesa.getGanador()
            self.ganador_por_mano.append(ganador_mano)
            if ganador_mano != None and ganador_mano != self.jugador_actual:
                self.cambiar_turno()

    def cantar_envido(self, tipo_envido: str) -> None:
        """
        Canta el envido, creando el objeto que representa el envido actual, y
        cambiando el turno del jugador actual. Si el jugador actual ya canto el envido,
        actualiza el envido actual siempre que sea valido el proximo estado

        Precondiciones:

        * El tipo de envido es un string que representa el tipo de envido a cantar
        * El jugador actual y el contrario son una instancia de la clase `Jugador`

        Postcondiciones:

        * `self.envido` es una instancia de la clase `Envido` que representa el envido actual
        * Se cambia el turno de los jugadores
        """
        
        if self.jugador_canto_envido == None:
            self.jugador_canto_envido = self.jugador_actual
            self.envido_actual = env.Envido(self.jugador_actual, self.jugador_contrario, tipo_envido, self.max_puntos)
            self.cambiar_turno()

        else:
            if self.envido_actual.actualizar(tipo_envido):
                self.cambiar_turno()

    def _resetear_envido(self) -> None:
        """
        Resetea el envido actual, usando el atributo `self.jugador_canto_envido` para
        saber quien canto el envido. Si el jugador actual no es el que canto el envido,
        cambia el turno del jugador actual

        Precondiciones:

        * El jugador actual y el contrario son una instancia de la clase `Jugador`

        Postcondiciones:

        * Se resetean los atributos `self.envido` y `self.jugador_canto_envido`
        """

        if self.jugador_actual != self.jugador_canto_envido:
            self.cambiar_turno()

        self.envido_actual = None
        self.jugador_canto_envido = None        

    def aceptar_envido(self) -> env.ResultadoEnvido:
        """
        Acepta el envido actual, y devuelve el resultado del envido actual dependiendo de
        quien haya ganado el envido, del jugador que es mano, y si fue falta envido parda 
        o no. Luego resetea el envido actual

        Precondiciones:

        * El envido es una instancia de la clase `Envido`

        Postcondiciones:

        * Se resetea el envido actual
        * Se devuelve el resultado del envido actual
        * Se suman los puntos correspondientes al jugador ganador
        """
        
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

    def rechazar_envido(self) -> None:
        """
        Rechaza el envido actual, y suma los puntos correspondientes al jugador contrario.

        Precondiciones:

        * El envido es una instancia de la clase `Envido`
        * El jugador contrario es una instancia de la clase `Jugador`

        Postcondiciones:

        * Se resetea el envido actual
        * Se suman los puntos correspondientes al jugador contrario
        """

        puntos = self.envido_actual.rechazar_envido()
        self.jugador_contrario.sumar_puntos(puntos)
        self._resetear_envido()

    def cantar_truco(self, tipo_truco: str) -> None:
        """
        Canta el truco, creando el objeto que representa el truco actual, y
        cambiando el turno del jugador actual. Si el jugador actual ya canto el truco,
        actualiza el truco actual siempre que sea valido el proximo estado

        Precondiciones:

        * El tipo de truco es un string que representa el tipo de truco a cantar

        Postcondiciones:

        * `self.truco_actual` es una instancia de la clase `Truco` que representa el truco actual
        * Se cambia el turno de los jugadores
        """

        if not self.truco_actual:
            self.truco_actual = truco.Truco(tipo_truco)

        else:
            self.truco_actual.actualizar(tipo_truco)
        
        self.cambiar_turno()

    def aceptar_truco(self) -> None:
        """
        Acepta el truco actual, para luego sumar los puntos correspondientes al jugador
        ganador. Cambia los turnos de ser necesario

        Precondiciones:

        * El truco es una instancia de la clase `Truco`

        Postcondiciones:

        * Se cambian los turnos de ser necesario
        """
        
        self.truco_actual.aceptar_truco()
        self.cambiar_turno() # cuidado que esto puede fallar 

    def _resetear_truco(self) -> None:
        """
        Resetea el truco actual

        Postcondiciones:

        * `self.truco_actual` es `None`
        """
        
        self.truco_actual = None

    def rechazar_truco(self) -> None:
        """
        Rechaza el truco actual, y suma los puntos correspondientes al jugador contrario.

        Precondiciones:

        * El truco es una instancia de la clase `Truco`

        Postcondiciones:

        * Se cambian los turnos de ser necesario
        """

        puntos = self.truco_actual.rechazar_truco()
        self.jugador_contrario.sumar_puntos(puntos)
        self.cambiar_turno()


    def iniciar_mano(self) -> None:
        """
        Inicia una mano, mezclando el mazo y repartiendo las cartas a los jugadores.
        Tambien se encarga de cambiar el turno del jugador que es mano, y de resetear
        los atributos `self.ganador_por_mano` y `self.ganador_final_mano`

        Precondiciones:

        * El mazo es una instancia de la clase `Mazo`
        * Los jugadores son instancias de la clase `Jugador`

        Postcondiciones:

        * Se mezcla el mazo
        * Se reparten las cartas a los jugadores
        * Se cambia el turno del jugador que es mano
        """

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
    
    
    def sumar_puntos_a_ganador(self) -> None:
        """
        Al finalizar una ronda, suma los puntos correspondientes al jugador ganador
        dependiendo de si se acepto el truco o no, y de quien gano la ronda

        Precondiciones:

        * El truco es una instancia de la clase `Truco`
        * El jugador ganador es una instancia de la clase `Jugador`
        * La ronda esta terminada

        Postcondiciones:

        * Se suman los puntos correspondientes al jugador ganador
        """

        if not self.ronda_esta_terminada():
            return
        
        if self.truco_actual and self.truco_actual.fue_aceptado():
            puntos = self.truco_actual.calcular_puntos()
            self.ganador_final_mano.sumar_puntos(puntos)
            self._resetear_truco()
            return

        self.ganador_final_mano.sumar_puntos(PUNTOS_RONDA_SIMPLE)


    def hay_ganador_ronda(self) -> None:
        """
        Devuelve `True` si hay un ganador de la ronda, y `False` en caso contrario, decidiendo
        el ganador de la ronda segun quien gano las manos
        """
        self.definir_ganador()
        return self.ganador_final_mano != None

    def definir_ganador(self) -> None:
        """
        Verifica todos los casos posibles para definir el ganador de la ronda, y guarda al 
        ganador en el atributo `self.ganador_final_mano

        Precondiciones:

        * Los jugadores son instancias de la clase `Jugador`
        * `self.ganador_por_mano` es una lista de jugadores que ganaron cada mano
        * `self.jugador_mano` es el jugador que es mano en la ronda actual

        Postcondiciones:

        * `self.ganador_final_mano` es el jugador que gano la ronda, None si todavia no hay ganador
        """
        def _triple_parda():
            """
            Devuelve si hubo triple parda en la ronda
            """
            
            return len(self.ganador_por_mano) == 3 and not self.jugador_actual in self.ganador_por_mano and not self.jugador_contrario in self.ganador_por_mano

        def _mismo_ganador_primeras_dos_manos() -> bool:
            """
            Devuelve si el mismo jugador gano las primeras dos manos
            """
            
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] == self.ganador_por_mano[1]

        def _parda_solo_en_segunda_mano() -> bool:
            """
            Devuelve si hubo parda solo en la segunda mano y alguien gano la primera
            """
            
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] != None and self.ganador_por_mano[1] == None

        def _ganador_en_tercera_mano_por_todo_parda() -> bool:
            """
            Devuelve si alguien gano la tercera mano y las dos primeras fueron parda
            """
            
            return len(self.ganador_por_mano) == 3 and self.ganador_por_mano[0] == None and self.ganador_por_mano[1] == None and self.ganador_por_mano[2] != None
        
        def _parda_solo_en_primera_mano() -> bool:
            """
            Devuelve si hubo parda solo en la primera mano y alguien gano la segunda
            """
            
            return len(self.ganador_por_mano) == 2 and self.ganador_por_mano[0] == None and self.ganador_por_mano[1] != None
            
        def _ganador_en_tercera_mano_sin_parda() -> bool:
            """
            Devuelve si alguien gano la tercera mano y ninguna de las dos primeras fueron parda
            """
            
            return len(self.ganador_por_mano) == 3 and self.ganador_por_mano[0] != None and self.ganador_por_mano[1] != None and self.ganador_por_mano[2] != None
        
        def _ganador_en_tercera_mano_por_parda() -> bool:
            """
            Devuelve si alguien gano la tercera mano siendo esta ultima parda
            """
            
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
        
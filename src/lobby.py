
class Lobby(): 
    """
    Clase que representa al lobby del juego. Este permite al usuario  elegir:
        - Con que personaje jugar
        - Contra que personaje jugar
        - A cuatos puntos se juega : 15, 30
        - Si se juega con flor o sin flor
        - Iniciar una partida
    """

    def __init__(self) -> None:
        """
        Crea un lobby para jugar al truco
        """

        self.personaje = None
        self.personaje_oponente = None
        self.puntos = None
        self.flor = None
        self.partida = None

    def seleccionar_personaje(self, personaje: str) -> None: 
        """
        Recibe un string con el nombre del personaje y lo asigna al atributo personaje
        """
        self.personaje = personaje
    
    def seleccionar_personaje_oponente(self, personaje: str) -> None: 
        """
        Recibe un string con el nombre del personaje y lo asigna al atributo personaje_oponente
        """
        self.personaje_oponente = personaje

    def seleccionar_puntos(self, puntos: int) -> None:
        """
        Recibe un int con la cantidad de puntos y lo asigna al atributo puntos

        Los puntos permitidos son 15 y 30
        """
        if puntos not in [15, 30]: raise PuntosInvalidosError("Los puntos deben ser 15 o 30")
        self.puntos = puntos
    
    def seleccionar_flor(self, flor: bool) -> None:
        """
        Recibe un bool con la opcion de flor y lo asigna al atributo flor
        """
        self.flor = flor

    def iniciar_partida(self) -> None:
        """
        Inicia una partida con los parametros seleccionados, para ello llama a una instancia
        de a clase Partida y la inicia con los valores obtenidos.
        """
        if self.personaje is None or self.personaje_oponente is None or self.puntos is None or self.flor is None:
            raise CamposIncompletos("Faltan campos por completar")

        # Aca se llama a la clase Partida y se inicia la partida

class PuntosInvalidosError(Exception):
    def __init__(self, mensaje: str) -> None:
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class CamposIncompletos(Exception):
    def __init__(self, mensaje: str) -> None:
        self.mensaje = mensaje
        super().__init__(self.mensaje)
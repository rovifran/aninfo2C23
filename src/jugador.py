import cartas

class Jugador:
    """
    Clase que representa a un jugador del Truco Argentino.
    Mantiene las cartas que tiene en la mano y los puntos que tiene acumulados.
    """
    def __init__(self, personaje):
        self.cartas = []
        self.puntos = 0
        self.personaje = personaje
        self.canto_truco_actual = "TRUCO"

    """
    Recibe las cartas que le tocan al jugador y las guarda en su mano.
    """
    def recibir_cartas(self, cartas):
        self.cartas = cartas

    """
    Juega una carta de su mano y la devuelve.
    """
    def jugar_carta(self, carta) -> cartas:
        self.cartas.remove(carta)
        return carta
    
    """
    Agrega los puntos al jugador.
    """
    def sumar_puntos(self, puntos):
        self.puntos += puntos
    
    """
    Pregunta si el jugador tiene los puntos necesarios para ganar.
    Devuelve True si los tiene, False en caso contrario.
    """
    def gano(self, max_puntos) -> bool:
        return self.puntos >= max_puntos
    
    def obtener_puntos(self) -> int:
        return self.puntos

    def obtener_cartas(self) -> list:
        return self.cartas

    def __str__(self):
        return self.personaje
    
    def __repr__(self):
        return self.personaje
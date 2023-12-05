from src import cartas

class Jugador:
    def __init__(self, personaje):
        self.cartas = []
        self.puntos = 0
        self.personaje = personaje

    def recibir_cartas(self, cartas):
        self.cartas = cartas

    def jugar_carta(self, carta) -> cartas:
        self.cartas.remove(carta)
        return carta
    
    def sumar_puntos(self, puntos):
        self.puntos += puntos
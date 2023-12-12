NO_QUIERO = "NO_QUIERO"

PUNTOS_Y_FASES = {
    "TRUCO": 2,
    "RETRUCO": 3,
    "VALE_CUATRO": 4,
    "NO_QUIERO": 1,
}

class Truco:

    def __init__(self, fase) -> None:
        self.fase = fase
        self.aceptado = False

    def calcular_puntos(self) -> int:
        return PUNTOS_Y_FASES[self.fase]

    def aceptar_truco(self) -> int:
        self.aceptado = True

    def rechazar_truco(self) -> int:
        self.fase = NO_QUIERO
        self.aceptado = False
        return self.calcular_puntos()

    def actualizar(self, fase: str) -> None:
        self.fase = fase

    def fue_aceptado(self):
        return self.aceptado
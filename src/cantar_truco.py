
NO_QUIERO = "NO_QUIERO"

PUNTOS_Y_FASES = {
    "TRUCO": 2,
    "RETRUCO": 3,
    "VALE_CUATRO": 4,
    "NO_QUIERO": 1,
}

class Truco:

    def __init__(self, fase, jugador) -> None:
        self.fase = fase
        self.aceptado = False
        self.fase_anterior = "NO_QUIERO"
        self.ultimo_que_canto = None
        self.canto_truco = jugador


    def calcular_puntos(self) -> int:
        if self.fue_aceptado():
            return PUNTOS_Y_FASES[self.fase]
        return PUNTOS_Y_FASES[self.fase_anterior]

    def aceptar_truco(self) -> int:
        self.aceptado = True

    def rechazar_truco(self) -> int:
        self.fase = NO_QUIERO
        self.aceptado = False
        return self.calcular_puntos()

    def actualizar(self, fase: str, jugador = None) -> None:
        if jugador: 
            self.canto_truco = jugador
            
        self.fase_anterior = self.fase
        self.fase = fase

    def fue_aceptado(self):
        return self.aceptado
    
    def obtener_canto_truco(self):
        return self.canto_truco
    
    
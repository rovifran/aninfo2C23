#import jugador
ACCIONES_CAMBIAN_TURNO = ['Jugar Carta']
ACCIONES_NO_CAMBIAN_TURNO = ['Cantar Truco', 'Cantar Re Truco', 'Cantar Vale Cuatro', 'Irse al Mazo', 'Envido', 'Real Envido', 'Falta Envido', 'Quiero']
RESPUESTA_BORDE = ['No Quiero', 'Irse al Mazo']
ACCIONES_REQUIEREN_RTA = ['Cantar Truco', 'Cantar Re Truco', 'Cantar Vale Cuatro', 'Envido', 'Real Envido', 'Falta Envido']

class Mano:
    def __init__(self, j_act, j_cont, ganador) -> None:
        self.j_act = None
        self.j_cont = None
        self.ganador = None

    def jugar(self, accion):
        accion = self.j_act.ejecutar_accion(accion)
        if accion in ACCIONES_REQUIEREN_RTA:
            self.j_cont.esperar_respuesta()

    def sumar_puntos_a_jugador(self, jugador, puntos):
        self.jugador.sumar_puntos(puntos)
        
    
from cartas import *

class Mazo() :
    def __init__(self):
        self.cartas = [
            AnchoDeEspada("1_esp.png"),
            AnchoDeBasto("1_bas.png"),
            SieteDeEspada("7_esp.png"),
            SieteDeOro("7_oro.png"),
            AnchoFalso("1_oro.png"),
            AnchoFalso("1_copa.png"),
            SieteFalso("7_basto.png"),
            SieteFalso("7_copa.png"),
            Dos("2_esp.png"),
            Dos("2_bas.png"),
            Dos("2_oro.png"),
            Dos("2_copa.png"),
            Tres("3_esp.png"),
            Tres("3_bas.png"),
            Tres("3_oro.png"),
            Tres("3_copa.png"),
            Doce("12_esp.png"),
            Doce("12_bas.png"),
            Doce("12_oro.png"),
            Doce("12_copa.png"),
            Once("11_esp.png"),
            Once("11_bas.png"),
            Once("11_oro.png"),
            Once("11_copa.png"),
            Diez("10_esp.png"),
            Diez("10_bas.png"),
            Diez("10_oro.png"),
            Diez("10_copa.png"),
            Seis("6_esp.png"),
            Seis("6_bas.png"),
            Seis("6_oro.png"),
            Seis("6_copa.png"),
            Cinco("5_esp.png"),
            Cinco("5_bas.png"),
            Cinco("5_oro.png"),
            Cinco("5_copa.png"),
            Cuatro("4_esp.png"),
            Cuatro("4_bas.png"),
            Cuatro("4_oro.png"),
            Cuatro("4_copa.png")
        ]
    
print("antes de mazo()")
Mazo()
print("despues de mazo()")
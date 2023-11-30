from typing import Tuple
from enum import Enum
import pygame
import os

# Obtenemos el directorio actual para poder acceder a las imagenes de las cartas
CUR_DIR = os.getcwd()

# Prioridades de las cartas. Las prioridades mas bajas ganan por sobre las mas altas
PRIORIDAD_ANCHO_DE_ESPADA = 1
PRIORIDAD_ANCHO_DE_BASTO = 2
PRIORIDAD_SIETE_DE_ESPADA = 3
PRIORIDAD_SIETE_DE_ORO = 4
PRIORIDAD_TRES = 5
PRIORIDAD_DOS = 6
PRIORIDAD_ANCHO_FALSO = 7
PRIORIDAD_DOCE = 8
PRIORIDAD_ONCE = 9
PRIORIDAD_DIEZ = 10
PRIORIDAD_SIETE_FALSO = 11
PRIORIDAD_SEIS = 12
PRIORIDAD_CINCO = 13
PRIORIDAD_CUATRO = 14

def obtener_palo_y_numero(ruta_imagen: str) -> Tuple:
    """
    Dada una ruta de imagen, devuelve una tupla con el numero y el palo de la carta. 
    
    Precondiciones:
    * La ruta pasada por parametro es valida
    * La ruta pasada por parametro es de una imagen de una carta

    Postcondiciones:
    * Devuelve una tupla con el numero y el palo de la carta
    """
    numero, palo = ruta_imagen.split('.')[0].split('_')
    return int(numero), palo

class _Carta:
    """
    Clase abstracta que representa una carta del truco. No se puede instanciar directamente.
    Define metodos de comparacion que se usan para determinar que carta gana en una mano.

    Atributos:
    * numero: Entero que representa el numero de la carta
    * palo: String que representa el palo de la carta
    * _prioridad: Entero que representa la prioridad de la carta, con la finalidad de compararlas
    * imagen: Imagen de la carta, cargada con pygame. Se usa para mostrar la carta en pantalla
    """
    def __init__(self, ruta_imagen: str, prioridad: int) -> None:
        """
        Inicializa una carta con la ruta de la imagen y la prioridad pasadas por parametro.
        Este metodo de instanciacion es utilizado por las subclases de Carta

        Precondiciones:
        * La ruta pasada por parametro es valida
        * La prioridad corresponde a la prioridad de la carta en cuestion

        Postcondiciones:
        * Se inicializa una carta con la ruta de la imagen y la prioridad pasadas por parametro
        """
        numero, palo = obtener_palo_y_numero(ruta_imagen)
        self.numero = numero
        self.palo = palo
        self._prioridad = prioridad
        self.imagen = pygame.image.load(CUR_DIR + '/cartas/' + ruta_imagen)

    def mostrar_imagen(self) -> pygame.Surface:
        """
        Devuelve la imagen de la carta
        """
        return self.imagen

    def __gt__(self, otra: '_Carta') -> bool:
        """
        Sobrecarga el operador > para comparar dos cartas segun su prioridad
        """
        return self._prioridad < otra._prioridad
    
    def __ge__(self, otra: '_Carta') -> bool:
        """
        Sobrecarga el operador >= para comparar dos cartas segun su prioridad
        """
        return self._prioridad <= otra._prioridad
    
    def __eq__(self, otra: '_Carta') -> bool:
        """
        Sobrecarga el operador == para comparar dos cartas segun su prioridad
        """
        return self._prioridad == otra._prioridad
    
    def __lt__(self, otra: '_Carta') -> bool:
        """
        Sobrecarga el operador < para comparar dos cartas segun su prioridad
        """
        return self._prioridad > otra._prioridad
    
    def __le__(self, otra: '_Carta') -> bool:
        """
        Sobrecarga el operador <= para comparar dos cartas segun su prioridad
        """
        return self._prioridad >= otra._prioridad

class AnchoDeEspada(_Carta):
    """
    Subclase de _Carta que representa la carta Ancho de Espada.
    """
    
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Ancho de Espada con la ruta de la imagen y la prioridad
        correspondiente al Ancho de Espada
        """    
        super().__init__(ruta, PRIORIDAD_ANCHO_DE_ESPADA)

class AnchoDeBasto(_Carta):
    """
    Subclase de _Carta que representa la carta Ancho de Basto.
    """

    def __init__(self, ruta: str) -> None: 
        """
        Inicializa una carta Ancho de Espada con la ruta de la imagen y la prioridad
        correspondiente al Ancho de Basto
        """
        super().__init__(ruta, PRIORIDAD_ANCHO_DE_BASTO)
    
class SieteDeEspada(_Carta):
    """
    Subclase de _Carta que representa la carta Siete de Espada.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Siete de Espada con la ruta de la imagen y la prioridad
        correspondiente al Siete de Espada
        """
        super().__init__(ruta, PRIORIDAD_SIETE_DE_ESPADA)

class SieteDeOro(_Carta):
    """
    Subclase de _Carta que representa la carta Siete de Oro.
    """
    
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Siete de Oro con la ruta de la imagen y la prioridad
        correspondiente al Siete de Oro
        """
        super().__init__(ruta, PRIORIDAD_SIETE_DE_ORO)

class Tres(_Carta):
    """
    Subclase de _Carta que representa las distintas cartas con el numero Tres.
    """
    
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Tres con la ruta de la imagen y la prioridad
        correspondiente al Tres.
        """
        super().__init__(ruta, PRIORIDAD_TRES)

class Dos(_Carta):
    """
    Subclase de _Carta que representa las distintas cartas con el numero Dos.
    """
    
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Dos con la ruta de la imagen y la prioridad
        correspondiente al Dos.
        """
        super().__init__(ruta, PRIORIDAD_DOS)

class AnchoFalso(_Carta):
    """
    Subclase de _Carta que representa a los Anchos Falsos (Ancho de Oro y Ancho de Copa).
    """
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Ancho Falso con la ruta de la imagen y la prioridad
        correspondiente al Ancho Falso.
        """
        super().__init__(ruta, PRIORIDAD_ANCHO_FALSO)

class Doce(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Doce.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Doce con la ruta de la imagen y la prioridad
        correspondiente al Doce.
        """
        super().__init__(ruta, PRIORIDAD_DOCE)

class Once(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Once.
    """
    
    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Once con la ruta de la imagen y la prioridad
        correspondiente al Once.
        """
        super().__init__(ruta, PRIORIDAD_ONCE)

class Diez(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Diez.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Diez con la ruta de la imagen y la prioridad
        correspondiente al Diez.
        """
        super().__init__(ruta, PRIORIDAD_DIEZ)

class SieteFalso(_Carta):
    """
    Subclase de _Carta que representa a los Sietes Falsos (Siete de Copa y Siete de Basto).
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Siete Falso con la ruta de la imagen y la prioridad
        correspondiente al Siete Falso.
        """
        super().__init__(ruta, PRIORIDAD_SIETE_FALSO)

class Seis(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Seis.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Seis con la ruta de la imagen y la prioridad
        correspondiente al Seis.
        """
        super().__init__(ruta, PRIORIDAD_SEIS)

class Cinco(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Cinco.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Cinco con la ruta de la imagen y la prioridad
        correspondiente al Cinco.
        """
        super().__init__(ruta, PRIORIDAD_CINCO)

class Cuatro(_Carta):
    """
    Subclase de _Carta que representa a las distintas cartas con el numero Cuatro.
    """

    def __init__(self, ruta: str) -> None:
        """
        Inicializa una carta Cuatro con la ruta de la imagen y la prioridad
        correspondiente al Cuatro.
        """
        super().__init__(ruta, PRIORIDAD_CUATRO)

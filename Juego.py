#Se importa la librería abc para la creacion de clases y métodos abstractos
import abc
from abc import ABC
#Se importa la librería random para utilizarla cuandos se acceda al método ReiniciaPartida
from random import *

class Juego(ABC):
#Al lado del número 7 se observan las clases hijas que hereda la súper clase o clase padre
    _num = int(0)
    _numVidas = int(0)
    _intentos = int(0)

    """
    Se declaró el método Juega como método abstracto para que ninguna instancia acceda al mismo 
    y en este caso no toma parámetros y retorna un cero.
    """
    @abc.abstractmethod
    def Juega(self):
        return 0

    """
    Se declaró el método QuitaVida para quitarle una vida al usuario cuando se equivoque al intentar adivinar el número 
    y este método devuelve un boolean de tipo True si el número de vidas es mayor a cero lo que permite continuar con la 
    ejecución del programa y devuelve False cuando se le hayan acabado las vidas.
    """
    def QuitaVida(self):
        self._numVidas = self._numVidas - 1
        if self._numVidas > 0:
            return True
        else:
            return False
    """
    Se declaró el método ReiniciaPartida para volver a ejecutar el programa cuando el número de vidas llegue a cero y el 
    usuario introduzca que quiere volver a intentarlo.
    """
    def ReiniciaPartida(self):
        self._numVidas = 3
        self._num = randrange(10)
        self._intentos = 0
        self.Juega()

    """
    Declaración del método ActualizaRecord, que se encarga de aumentarle el récord al usuario, y cada vez que 
    se equivoque le aumente el récord y también cuando acierte acceda a este método.
    """
    def ActualizaRecord(self):
        self._intentos = self._intentos + 1
from random import *
from JuegoAdivinaNumero import *
from JuegoAdivinaPar import *
from JuegoAdivinaImpar import *
"""
Archivo Aplicacion dónde se importa el contenido de los archivos JuegoAdivinaNumero, JuegoAdivinaPar, JuegoAdivinaImpar,
para generarles una instancia o un objeto que acceda a ellos y también se importa la librería random para que la 
consola le genere un número aleatorio comprendido del 0 al 10 para que el usuario lo adivine.

Aquí se implementa el método main() dónde el usuario selecciona el tipo de juego mediante sentencias if y elif, 
en este método es dónde se crean las instancias que acceden a las respectivas clases JuegoAdivinaNumero, 
JuegoAdivinaPar, JuegoAdivinaImpar, creándoles los parámetros del método constructor y después accediendo al método 
Juega del tipo de juego seleccionado por el usuario y añadiéndole una sentencia while que se cumpla siempre y cúando 
el usuario haya perdido quiera volver a intentarlo.
"""

def main():

    s = int(input(
        'Seleccione el tipo de Juego: \n 1 = Adivina Número \n 2 = Adivina Número Par \n 3 = Adivina Número Impar \n'))

    if s == 1:
        juega = JuegoAdivinaNumero(randrange(10), 3)
        juega.Juega()

    elif s == 2:
        juega = JuegoAdivinaPar(choice([0, 2, 4, 6, 8, 10]), 3)
        juega.Juega()

    elif s == 3:
        juega = JuegoAdivinaImpar(choice([1, 3, 5, 7, 9]), 3)
        juega.Juega()

    while True:
        r = input('¿Quieres volver a intentar? \n Introduce: \ns = para seguir Jugando \nn = para salir ')

        if r == "s":
            juega.ReiniciaPartida()
        else:
            if r == "n":
                print("\n Gracias por jugar :)")
                break
            else:
                print('No entendí vuelve a rectificar, asegúrate escribir en minúsculas.')

if __name__ == '__main__':
    main()
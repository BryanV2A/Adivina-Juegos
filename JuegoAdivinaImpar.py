from JuegoAdivinaNumero import *

"""
línea 1 = importación de todo el archivo JuegoAdivinaNumero

línea 9 = Clase JuegoAdivinaPar hereda de la súper clase JuegoAdivinaNumero
"""

class JuegoAdivinaImpar(JuegoAdivinaNumero):

    """
    Sobre escritura 'Override' del método ValidaNumero heredado de la clase padre JuegoAdivinaNumero, aquí se
    vuelve a implementar el ejercicio 2, se redefine el método para generarle un rango al número introducido por el
    usuario ya que solo debe introducir los números impares del 0 al 10 y el programa no le restara vidas ni le
    actualizara el record si esto no se cumple muestra un mensaje de error.

    """

    def ValidaNumero(self, num):

        if num % 2 != 0 and num > 0 and num < 10:
            return True
        else:
            print('Error!! El número debe de ser un número Impar del 0 al 10')
            return False
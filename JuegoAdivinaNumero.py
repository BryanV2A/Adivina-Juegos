from Juego import *
#Del archivo Juego importa su contenido

class JuegoAdivinaNumero(Juego):
#la clase JuegoAdivinaNumero deriva de la clase padre Juego, dejándolo acceder a su contenido.

    """
    Declaración del método constructor que toma como parámetros el número ingresado por el usuario y el número
    de vidas ya definido.
    """

    def __init__(self, num, numVidas):

        self._num = num
        self._numVidas = numVidas

    """
    Sobre escritura 'Override' del método Juega heredado de la clase padre Juego, que se encarga de toda la ejecución
    del programa imprimiendo mensajes para la introducción de valores e indicaciones para el usuario
    y mostrando mensajes que retornan valores.
    """
    def Juega(self):
        print('Estoy pensando en un número del 0 al 10 ¿Puedes adivinarlo?: ')
        while self._numVidas:

            print('\nNúmero de vidas:', self._numVidas)
            #Mnesaje que muestra el número de vidas del usuario
            num = int(input('\n Intruduce el número: '))
            """
            Línea 33: Condicional if que accede o realiza un salto al método ValidaNumero que está declarado más 
            abajo, y se ejecuta esa condición siempre y cuando sea verdadera.
            """
            if self.ValidaNumero(num):
                    """
                    Sentencia if que evalúa la condición 'Si el número introducido por el usuario es igual al número 
                    generado por la consola' y realiza la acción de realizar un salto al método ActualizaRecord e 
                    imprimir un mensaje de que acertó en el número.
                    """
                    if (num == self._num):
                        self.ActualizaRecord()
                        print('\n Acertaste!!, En el intento:', self._intentos, ', El numero era:', self._num)
                        break
                    else:
                        """
                        Si no es así accede al método ActualizaRecord y realiza la condicional if que accede o realiza 
                        un salto al método QuitaVida heredado y mientras este sea verdadero realiza otras dos 
                        condiciones que evalúan si el numero introducido es mayor o menor que el numero generado. 
                        """
                        self.ActualizaRecord()
                        if self.QuitaVida():
                            if (num > self._num):
                                print('Lo siento vuelvelo a intentar el número es menor a', num)
                            if (num < self._num):
                                print('Lo siento vuelvelo a intentar el número es mayor a', num)

                            """
                            La condición if accede al método QuitaVida y si este devuelve un boolena tipo False 
                            imprime un mensaje indicándole al usuario que ha perdido.
                            """
                        else:
                            print('Lo siento has perdido, el número era ', self._num)

            else:
                """
                Si la condición del ValidaNumero no es cumplida muestra un mensaje de error 
                """
                print('Error!! Vuelve a introducir el número')

    """
    Método ValidaNumero que se supone que siempre devolvería True, pero se le agregó el extra de generarle un rango  
    con una sentencia if al número introducido por el usuario para que no fuera mayor que 10 ni menor que 0 y que el 
    programa no le restara vidas ni le actualizara el record, si no cumplía con esta condición imprime un mensaje.
    """
    def ValidaNumero(self, num):
        if num >= 0 and num <= 10:
            return True
        else:
            print('El número debe de ser del 0 al 10')
            return False
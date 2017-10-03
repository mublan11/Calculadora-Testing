import math
"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 06/SEP/17
"""
class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = num1 + num2    
        except:
            self.resultado = 'Datos incorrectos'

    def resta(self, num1, num2):
        try:
            self.resultado = num1 - num2
        except:
            self.resultado = 'Datos incorrectos'

    def division(self, num1, num2):
        try:
            if num2 == 0:
                self.resultado = "La division por cero no esta definida"
            else:
                self.resultado = num1 / num2
        except:
            self.resultado = 'Datos incorrectos'
    
    def multiplicacion(self, num1, num2):
        try:                    
            if type(num1) == str or type(num2) == str:
                self.resultado = "Datos incorrectos"
            else:
                self.resultado = num1 * num2
        except:
            self.resultado = 'Datos incorrectos'    

    def potencia(self, num1, num2):
        try:                    
            if type(num1) == str or type(num2) == str:
                self.resultado = "Datos incorrectos"
            else:
                self.resultado = num1 ** num2
        except:
            self.resultado = 'Datos incorrectos'

    def raiz(self, num1):
        try:
            if num1 < 0:
                self.resultado = "No se aceptan numeros negativos (i)"
            elif type(num1) == str:
                self.resultado = "Datos incorrectos"
            else:
                self.resultado = math.sqrt(num1)
        except:
            self.resultado = 'Datos incorrectos'
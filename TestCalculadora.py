import unittest
from calculadora import Calculadora
"""
	Autor: Diego Misael Blanco Murillo.
	Fecha: 06/SEP/17
"""
#Comentario para probar Travis
class CalculadoraTest(unittest.TestCase):
	
	def setUp(self):
		self.calc = Calculadora()
		self.datosIncorrectos = 'Datos incorrectos'

	def test_valor_de_inicio_igual_a_cero(self):	
		self.assertEquals(self.calc.obtener_resultado(), 0)
	
	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 4)

	def test_sumar_3_mas_3_igual_6(self):
		self.calc.suma(3,3)
		self.assertEquals(self.calc.obtener_resultado(), 6)

	def test_sumar_menos_uno_mas_2_igual_1(self):
		self.calc.suma(-1,2)
		self.assertEquals(self.calc.obtener_resultado(), 1)
	
	def test_sumar_ele_mas_2_igual_datos_incorrectos(self):
		self.calc.suma('L',2)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def test_restar_2_menos_2_igual_0(self):
		self.calc.resta(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_restar_3_menos_9_igual_menos_6(self):
		self.calc.resta(3,9)
		self.assertEquals(self.calc.obtener_resultado(), -6)
	
	def test_restar_menos_1_menos_2_igual_menos_3(self):
		self.calc.resta(-1,2)
		self.assertEquals(self.calc.obtener_resultado(), -3)

	def test_restar_2_menos_10_igual_menos_8(self):
		self.calc.resta(2,10)
		self.assertEquals(self.calc.obtener_resultado(), -8)

	def test_restar_uve_menos_2_igual_datos_incorrectos(self):
		self.calc.resta('V',2)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def test_dividir_2_entre_2_igual_1(self):
		self.calc.division(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 1)

	def test_dividir_99_entre_5_igual_19(self):
		self.calc.division(99,5)
		self.assertEquals(self.calc.obtener_resultado(), 19)

	def test_dividir_menos_88_entre_78_igual_menos_2(self):
		self.calc.division(-88,78)
		self.assertEquals(self.calc.obtener_resultado(), -2)

	def test_dividir_0_entre_11_igual_0(self):
		self.calc.division(0,11)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_dividir_10_entre_0_igual_division_no_definida(self):
		self.calc.division(10,0)
		self.assertEquals(self.calc.obtener_resultado(), 'La division por cero no esta definida')

	def test_dividir_eme_entre_2_igual_datos_incorrectos(self):
		self.calc.division('M',2)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def test_multiplicar_5_por_5_igual_25(self):
		self.calc.multiplicacion(5,5)
		self.assertEquals(self.calc.obtener_resultado(), 25)

	def test_multiplicar_menos_11_por_menos_23_igual_253(self):
		self.calc.multiplicacion(-11,-23)
		self.assertEquals(self.calc.obtener_resultado(), 253)

	def test_multiplicar_11_por_menos_11_igual_menos_121(self):
		self.calc.multiplicacion(11,-11)
		self.assertEquals(self.calc.obtener_resultado(), -121)

	def test_multiplicar_zeta_por_2_igual_datos_incorrectos(self):
		self.calc.multiplicacion('Z',2)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)
	
	def test_multiplicar_10_por_0_igual_0(self):
		self.calc.multiplicacion(10,0)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_elevar_2_a_la_3_igual_8(self):
		self.calc.potencia(2,3)
		self.assertEquals(self.calc.obtener_resultado(), 8)
	
	def test_elevar_10_a_la_menos_4_igual_punto_0001(self):
		self.calc.potencia(10,-4)
		self.assertEquals(self.calc.obtener_resultado(), 0.0001)

	def test_elevar_de_a_la_11_igual_datos_incorrectos(self):
		self.calc.potencia('D',11)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)
	
	def test_elevar_menos_1_a_la_punto_5_igual_datos_incorrectos(self):
		self.calc.potencia(-1,0.5)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def test_elevar_menos_9_a_la_punto_5_igual_datos_incorrectos(self):
		self.calc.potencia(-9,0.5)
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def test_raiz_8_igual_2_punto_8284271247461903(self):
		self.calc.raiz(8)
		self.assertEquals(self.calc.obtener_resultado(), 2.8284271247461903)

	def test_raiz_0_igual_0(self):
		self.calc.raiz(0)
		self.assertEquals(self.calc.obtener_resultado(), 0)
	
	def test_raiz_78_punto_54_igual_8_punto_86227961644181(self):
		self.calc.raiz(78.54)
		self.assertEquals(self.calc.obtener_resultado(), 8.86227961644181)

	def test_raiz_menos_11_igual_no_numeros_negativos(self):
		self.calc.raiz(-11)
		self.assertEquals(self.calc.obtener_resultado(), 'No se aceptan numeros negativos (i)')

	def test_raiz_eme_datos_incorrectos(self):
		self.calc.raiz('M')
		self.assertEquals(self.calc.obtener_resultado(), self.datosIncorrectos)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
# -*- coding: utf-8 -*-

"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 01/OCT/17
"""

from lettuce import step, world
from calculadora import Calculadora

@step(u'cuando realizo la operacion entonces')
def cuando_realizo_la_operacion_entonces(step):
    pass

#Para suma
@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))

@step(u'obtengo el resultado "([^"]*)"')
def obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido, 'El resultado esperado es '+esperado+' y el obtenido es '+str(obtenido)

#Para resta
@step(u'Dado que incorporo los numeros "([^"]*)" y "([^"]*)"')
def dado_que_incorporo_los_numeros_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

#Para multiplicacion
@step(u'Dado que multiplico los numeros "([^"]*)" y "([^"]*)"')
def dado_que_multiplico_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

#Para division
@step(u'Dado que divido los numeros "([^"]*)" y "([^"]*)"')
def dado_que_divido_los_numeros_group1_y_group2(step, num1, num2):
	world.cal = Calculadora()
	world.cal.division(int(num1), int(num2))

#Para potencia
@step(u'Dado que elevo los numeros "([^"]*)" y "([^"]*)"')
def dado_que_elevo_los_numeros_group1_y_group2(step, num1, num2):
	world.cal = Calculadora()
	world.cal.potencia(int(num1), int(num2))

#Para raiz
@step(u'Dado que logro la raiz de "([^"]*)"')
def dado_que_logro_la_raiz_de_group1(step, num1):
	world.cal = Calculadora()
	world.cal.raiz(int(num1))
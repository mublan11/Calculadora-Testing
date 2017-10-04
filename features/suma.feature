Feature: Suma de dos numeros
	Como usuario de la calculadora
	deseo realizar la suma de dos numeros
	para obtener el resultado preciso

	Scenario: Suma de 2 mas 2
		Dado que ingreso los numeros "2" y "2"
		cuando realizo la operacion entonces 
		obtengo el resultado "4"

	Scenario: Suma de 7 mas 5
		Dado que ingreso los numeros "7" y "5"
		cuando realizo la operacion entonces 
		obtengo el resultado "12"

	Scenario: Suma de 0 mas -7
		Dado que ingreso los numeros "0" y "-7"
		cuando realizo la operacion entonces 
		obtengo el resultado "-7"

	Scenario: Suma de 1000 mas 100
		Dado que ingreso los numeros "1000" y "100"
		cuando realizo la operacion entonces 
		obtengo el resultado "1100"
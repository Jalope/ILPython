#Podemos volver a introducir las cosas pero entramos en bucle infinito aunque introduzcamos bien las cosas
while (True):
	try:
		a = float(input("Introduce un numero: "))
		b = 10 / a
		print(10/a)
	#De esta forma nos enseña el tipo del error que se comete
	except:
		print("Por lo que sea eres un poco tonto")
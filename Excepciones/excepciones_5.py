#Podemos volver a introducir las cosas sin entrar en bucles
while (True):
	try:
		a = float(input("Introduce un numero: "))
		b = 10 / a
		print(10/a)
		break
	#De esta forma nos enseña el tipo del error que se comete
	except:
		print("Por lo que sea eres un poco tonto")
	finally: 
		print("Va igual no eres tan bobo")
		break
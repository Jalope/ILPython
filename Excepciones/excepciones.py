#Pase lo que pase solo se ejecuta 1 vez
try:
	a = float(input("Introduce un numero: "))
	b = 10 / a
	print(10/a)
#De esta forma nos enseña el tipo del error que se comete
except:
	print("Por lo que sea eres un poco tonto")
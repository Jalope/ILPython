#tipo de error
try:
	a = float(input("Introduce un numero: "))
	b = 10 / a
	print(10/a)
#De esta forma nos enseña el tipo del error que se comete
except Exception as x:
	print(type(x).__name__)
	print("Por lo que sea eres un poco tonto")


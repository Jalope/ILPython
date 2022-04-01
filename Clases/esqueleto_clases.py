class Alumno: #en todos los metodos, incluido el constructor hay que pasar self. 
    #constructor. Contiene los atributos de la clase 
    def __init__(self, nombre): 
        self.nombre = nombre #se define de esta manera para no perder la variable ni entre metodos dentro de la clase ni fuera de ella

        
    #metodo es cada una de las funciones
    def saludar(self): 
        print(f"Hola!, {self.nombre}")
    
#HERENCIA

class Poligono: 
    """
    Define un poligono según su base y su altura
    """
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura 

class Rectangulo(Poligono): 
    def area(self): 
        return self.base * self.altura

class Triangulo(Poligono): 
    def area(self): 
        return (self.base * self.altura) / 2
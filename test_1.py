# Construccion de nuestro objeto e instancia de la clase

class Carro:

    ruedas = 4

    """Esto es el constructor de mi clase."""
    def __init__(self,color,aceleracion):
        self.color= color
        self.aceleracion= aceleracion
        self.velocidad = 0


    def acelera(self):
        self.velocidad=self.velocidad + self.aceleracion

    def frena(self):
        veloc=self.velocidad - self.aceleracion

        if veloc < 0:
            veloc = 0

        self.velocidad=veloc


"""""Instanciamos nuestro primer objeto"""

carro1= Carro("azul", 50)

print("El color de mi primer carro es : ", carro1.color)
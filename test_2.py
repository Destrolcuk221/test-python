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

carro1= Carro("rojo", 70)

print("El color de mi carro es : ", carro1.color)
print("La velocidad de mi carro es : ",carro1.velocidad)

carro1.acelera()
carro1.acelera()
print("La velocidad actual de mi carro es : ",carro1.velocidad)

carro1.frena()
carro1.frena()
print("La velocidad al frenar mi carro es : ",carro1.velocidad)

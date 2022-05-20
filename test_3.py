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
carro2= Carro("Azul",60)

print(carro1.color)
print(carro2.color)

carro1.marchas =6
print("Numero de marchas de mi primer carro : ",carro1.marchas)
#print("Numero de marchas de mi segundo carro : ",carro2.marchas)

carro2.marca="Toyota"

print("La marca de mi segundo carro es : ",carro2.marca)


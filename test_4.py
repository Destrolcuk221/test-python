""""Herencia en python"""

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

class CarroVolador(Carro):
    ruedas = 6

    def __init__(self,color,aceleracion,estado_volador=False):
        super().__init__(color,aceleracion)
        self.estado_volando=estado_volador

    def vuela(self):
        self.estado_volando=True

    def aterrizar(self):
        self.estado_volando=False

carro1 = Carro("Azul",40)
carroVolador1= CarroVolador("Rojo",60)

print(carroVolador1.color)
print(carroVolador1.estado_volando)

carroVolador1.acelera()
print("La velocidad de mi primer carro volador es : ",carroVolador1.velocidad)
print("La cantidad de  ruedas de mi carro volador es : ",carroVolador1.ruedas)
print("Estado de vuelo : ",carro1.estado_volando)


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

carro1 = Carro("Blanco",55)
print(type(carro1))

carroVolador =CarroVolador("Azul",60)
print(type(carroVolador))
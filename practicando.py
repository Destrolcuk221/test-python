class moto:

    ruedas = 2

    def __init__(self,color,aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad= 0

    def acelera(self):
      self.velocidad=self.aceleracion + self.velocidad

    def frena(self):
      veloc=self.aceleracion - self.velocidad
      if veloc < 0:
          veloc = 0


          self.velocidad=veloc

class MotoVolador(moto):
    ruedas = 3

    def __init__(self,color,aceleracion,estado_volador=False):
        super().__init__(color,aceleracion)
        self.estado_volando=estado_volador

    def vuela(self):
        self.estado_volando=True

    def aterriza(self):
        self.estado_volando=False

moto1=moto("rojo",55)
print(type(moto1))

MotoVolador = MotoVolador("azul",60)
print(type(MotoVolador))
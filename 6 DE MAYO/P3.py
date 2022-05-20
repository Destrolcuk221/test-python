"""""ENCAPSULAMIENTO EN PYTHON"""

class A:
    def __init__(self):
        self.contador=0
    def incrementa(self):


class B:
    def __init__(self):
           self.__contador = 0
    def incrementa(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador

variableA = A()
variableA.incrementa()
variableA.incrementa()
variableA.incrementa()

variableB = B()
variableB.incrementa()
variableB.incrementa()

print(variableB.cuenta())

print(variableB._B__contador)

# Crear una clase llamada circulo
# Que contenga un radio , con un metodo que devolvera el area.
# Y otro metodo que devolvera el perimetro del circulo
# Mostrar en consola el area de un circulo
# Mostrar el valor del perimetro del circulo

from math import  pi



class circulo():
    def __init__(self,radio):
        self.radio=radio

    def A(self):
        A=pi*self.radio**2
        print("El area equivale a : " , A)

    def π(self):
        π=2*pi*self.radio
        print("El perimetro es : ",π)

circulo1= circulo(2)
circulo1.A()
circulo1.π()

#PARA LA PRACTICA
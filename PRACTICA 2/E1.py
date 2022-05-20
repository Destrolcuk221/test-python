#Escriba un programa donde tendra los siguientes requisitos
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def nacion(self):
        self.nacionalidad="peruana"
    def incrementar_año(self):
        self._contador +=self.edad+ 1
    def edad_año(self):
        año1=self.edad + 1
        if año1 < 0:
            año1= +1
        self._contador=año1

try:
    nacion=input("Por favor ingrese su nacionalidad:  ")
except:
    print("No es de nacionalidad requerida,intente de nuevo ....",nacion)
#persona1=Persona(22,"peruana")
#print(type(persona1.nacionalidad()))
print("tipo de dato: ",type(nacion))







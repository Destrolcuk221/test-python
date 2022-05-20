class A:
    def imprimeA(self):
         print("a")

class B:
    def imprimeB(self):
           print("b")
""""HERENCIA MULTIPLE"""
class C(A,B):
    def imprimirC(self):
        print("c")



valorC= C()
valorC.imprimeA()
valorC.imprimeB()
valorC.imprimirC()



from LL import listaenlazada
from merkletree import MLKjunior
from bloqueBC import bloque
class blockchain:
    def __init__(self):
        self.Head = None
        self.actual = None
        self.index = 0
    def queputas(self,alv,puta):
        print("que putas"+alv+puta)


    def agrega_alv(self,trans,raiz):
        if self.Head == None:
            nuevo = bloque(self.index,trans,"-1",raiz)
            nuevo.work_hash('0')
            self.Head = nuevo
            self.actual = self.Head
            self.index = self.index +1
            print(nuevo)
            return True
        else:
            nuevo = bloque(self.index,trans,str(self.actual.hash),raiz)
            nuevo.work_hash('0')
            self.actual.next = nuevo
            self.actual = nuevo
            print(nuevo)
            return True
        



prueba = listaenlazada()
prueba.agrega_simple("compra")
prueba.agrega_simple("compra2")
prueba.agrega_simple("compra3")
prueba.agrega_simple("compra4")
print(prueba.head.value)
t = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
#bprueba = bloque(0,prueba,"hashprev",nodo)
mk = MLKjunior()
nodo2 = mk.merkle(t)

blo = blockchain()


blo.agrega_alv(prueba,nodo2)
blo.agrega_alv(prueba,nodo2)

        
            


            

            
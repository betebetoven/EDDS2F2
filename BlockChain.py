from LL import listaenlazada
from merkletree import MLKjunior
from bloqueBC import bloque
import os
import json

class blockchain:
    def __init__(self):
        self.Head = None
        self.actual = None
        self.index = 0
        self.primerizo = ""
    def queputas(self,alv,puta):
        print("que putas"+alv+puta)


    def agrega_alv(self,trans,raiz,opcional):
        if self.index == 0:
            nuevo = bloque(self.index,trans,"-1",raiz)
            nuevo.work_hash('0')
            self.Head = nuevo
            self.actual = self.Head
            self.index = self.index +1
            print(nuevo)
            return True
        elif self.index != 0 and self.Head!= None:
            nuevo = bloque(self.index,trans,str(self.actual.hash),raiz)
            nuevo.work_hash('0')
            self.actual.next = nuevo
            self.actual = nuevo
            self.index = self.index +1
            print(nuevo)
            return True
        elif self.index != 0 and self.Head== None:
            nuevo = bloque(self.index,trans,str(opcional),raiz)
            nuevo.work_hash('0')
            self.Head = nuevo
            self.actual = self.Head
            self.index = self.index +1
            print(nuevo)
            return True
    def graphviz(self):
        pepe = listaenlazada()
        general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = hexagon]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"
        dir_path = r'jsons\\'
        res = os.listdir(dir_path)
        if len(res)!=0:
            for n in res:
                with open(f'jsons/{n}') as json_file:
                    data = json.load(json_file)
                    prefdata = f'\"index:   {data["index"]}\ntimestamp: {str(data["timestamp"])}\nnonce:    {str(data["nonce"])}\nhash:  {str(data["data"]["self_hash"])}\nhashanterior: {str(data["data"]["hash_prev"])}\"'
                    pepe.agrega_simple(prefdata)
            k = pepe.head
            while k.Next != None:
                general+=f'\n{k.value}->{k.Next.value}'
                k=k.Next
            general+="\n}"
            f = open(f'BLOCKCHAIN.dot', "w")
            f.write(general)
            f.close()
            os.system(f'dot -Tpng BLOCKCHAIN.dot -o BLOCKCHAIN.png')


        
    def agrega_sinimprimir(self,trans,raiz):
        if self.Head == None:
            nuevo = bloque(self.index,trans,"-1",raiz)
            nuevo.work_hash('0')
            self.Head = nuevo
            self.actual = self.Head
            self.index = self.index +1
            #print(nuevo)
            return True
        else:
            nuevo = bloque(self.index,trans,self.primerizo,raiz)
            nuevo.work_hash('0')
            self.actual.next = nuevo
            self.actual = nuevo
            self.index = self.index +1
            #print(nuevo)
            return True
        


"""
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
"""
        
            


            

            
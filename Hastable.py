


from nodoLL import nodito
from prettytable import PrettyTable
import os

class jacinto():
    def __init__(self):
        self.head = None
        self.last = None
        self.tamaño = 13
        self.ocupacion = 0
        self.porcentaje_de_ocupacion = 0
        for n in range(self.tamaño):
            self.inicia_tamaño()
    def reinicio(self):
        self.head = None
        self.last = None
        self.tamaño = 13
        self.ocupacion = 0
        self.porcentaje_de_ocupacion = 0
        for n in range(self.tamaño):
            self.inicia_tamaño()

    def definir_porcentaje_ocupacion(self):
        self.porcentaje_de_ocupacion = self.ocupacion/self.tamaño
        return self.porcentaje_de_ocupacion    

    def inicia_tamaño(self):
        if self.head == None:
            self.head = nodito('')
            self.last = self.head
            self.head.Next = self.last
            self.last.Next = self.head
            self.colisiones = 0
        else:
            k = self.head
            
            while k.Next != self.head:
                #print(f'acaentra{k}')
                k = k.Next  
            k.Next = nodito('')
            self.last = k.Next
            self.last.Next = self.head
    def hasheo(self, cadena):
        general = sum(bytearray(cadena,encoding='utf-8'))
        #print(f'NUMEROHASH_____{general}')
        return general
    def agregar1(self, id,value):
        posicion = self.hasheo(str(id)+str(value)) % self.tamaño
       
        k = self.head
        for n in range(posicion):
            k = k.Next
        
        if k.value == "":
            print(f'SE VA A POSICION___{posicion}')
            k.value = value
            self.ocupacion = self.ocupacion +1
        else:
            print("HUBO OCOLISIOIN")
            f = k
            while f.value != "":
                
                posicion = posicion + 1
                
                f = f.Next
                if f == self.head:
                    posicion = 0
            print(f'SE VA A POSICION___{posicion}')
            f.value = value
            self.ocupacion = self.ocupacion+1
            
        print(f'PORCENTAJE DE OCUPACION____{str(self.definir_porcentaje_ocupacion()*100)}')
            #aca va la resolucion de colision
            
            #pass
    def retamaño(self):
        while self.definir_porcentaje_ocupacion()*100 > 20.00:
            self.agrega_vacios()
            print(f'PORCENTAJE DE OCUPACION____{str(self.definir_porcentaje_ocupacion()*100)}...%')
        print("retamaño:")
        #print(str(self))
        #self.prettytable(2)
    def agrega_vacios(self):
        k = self.head
            
        while k.Next != self.head:
                #print(f'acaentra{k}')
            k = k.Next  
        k.Next = nodito('')
        self.last = k.Next
        self.last.Next = self.head
        self.tamaño = self.tamaño+1
    def haseho2(self,numero):
        nuevo_index = ((numero % 3)+1)*self.colisiones
        return nuevo_index

    def agrega_inicial(self,id,value):
        posicion = self.hasheo(str(id)+str(value)) % self.tamaño
        self.agregar(id,value,posicion)



    def agregar(self,id,value,index):
        k = self.head
        for n in range(index):
            k = k.Next
        if k.value == "":
            #print(f'------------------------')
            print(f' ')
            print(f'[{value}] SE VA A POSICION___{index} que es la posicion {index % self.tamaño}')
            k.value = value
            print(k.value.__class__)
            self.ocupacion = self.ocupacion +1
            print(f'PORCENTAJE DE OCUPACION____{str(self.definir_porcentaje_ocupacion()*100)}...%')
            print(f'NUMERO DE COLISIONES____{str(self.colisiones)}')
            
            
            if self.definir_porcentaje_ocupacion()*100 > 80.0:
                print("YA SUPERO EL PORCENTAJE DE OCUPACION, DEBE AGRANDAR>>>>>>>>>>")
                self.retamaño()
            print(f' ')
            print("________________________")
        else:
            print(f'[{value}] SE HUBIERA IDO A POSICION___{index} que es la posicion {index % self.tamaño}')
            self.colisiones = self.colisiones + 1
            nuevo_index = self.haseho2(self.hasheo(str(id)+str(value)))
            self.agregar(id,value, nuevo_index+index)
            
        
            #aca va la resolucion de colision
            
            #pass
    
    def __str__(self) -> str:
        general = "TABLA HASH--------"
        k = self.head
        while k!= self.last:
            general+=f'\n{k}'
            k = k.Next
        general+=f'\n{self.last}'
        return general
    
    def prettytable(self,id):
        x = PrettyTable()
        x.field_names = ["index", "id", "value"]
        k = self.head
        for n in range(self.tamaño):
            x.add_row([n,id ,str(k.value)])
            k = k.Next
        print(x)
    def prettytable_llenos(self,id):
        graphvizx_dot = f'digraph G {"{"}\n a0 [shape= hexagon label=<\n<TABLE>\n<TR>\n<TD >"index"</TD>\n<TD >"id"</TD>\n<TD >"value"</TD>\n</TR>'
        x = PrettyTable()
        x.field_names = ["index", "id", "value"]
        k = self.head
        for n in range(self.tamaño):
            if k.value != "":
                x.add_row([n,id ,str(k.value)])
                graphvizx_dot+=f'<TR>\n<TD >"{n}"</TD>\n<TD >"{id}"</TD>\n<TD >"{str(k.value)}"</TD>\n</TR>'
            k = k.Next
        F = x.get_html_string()
        graphvizx_dot+=f'</TABLE>>];{"}"}'
        graphvizx = f'<!DOCTYPE html>\n<html>\n<title>CARRITO</title>\n<head>\n</head>\n<body>\n<h1>CARRITO</h1>\n<div>{F}</div>\n</body>\n</html>'
        
        f = open(f'CARRITO.dot', "w")
        f.write(graphvizx_dot)
        f.close()
        os.system(f'dot -Tpng CARRITO.dot -o CARRITO.png')
        file_html = open("CARRITO.html", "w")
        file_html.write(graphvizx)
        file_html.close()
        print(x)
    def total(self):
        k = self.head
        total = 0
        for n in range(self.tamaño):
            if k.value != "":
                total = total+k.value.precio
                #print(k.value.__class__)
            k = k.Next
        return total
    def toArray(self):
        x = []
        k = self.head
        for n in range(self.tamaño):
            if k.value != "":
                x.append(k.value)
            k = k.Next
        return x
    def eliminar(self,nombre):
        k = self.head
        while k.value== "" or k.value.nombre!=nombre:
            k=k.Next
        k.value = ""
        self.ocupacion = self.ocupacion -1

"""     
pedro = jacinto()
#print(f'tabla 1{pedro}')
pedro.prettytable(2)
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'b')
pedro.agrega_inicial(2,'c')
pedro.agrega_inicial(2,'d')
pedro.agrega_inicial(2,'e')
pedro.agrega_inicial(2,'f')
pedro.agrega_inicial(2,'g')
pedro.agrega_inicial(2,'h')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'a')

pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'b')
pedro.agrega_inicial(2,'c')
pedro.agrega_inicial(2,'d')
pedro.agrega_inicial(2,'e')
pedro.agrega_inicial(2,'f')
pedro.agrega_inicial(2,'g')
pedro.agrega_inicial(2,'h')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'a')

pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'b')
pedro.agrega_inicial(2,'c')
pedro.agrega_inicial(2,'d')
pedro.agrega_inicial(2,'e')
pedro.agrega_inicial(2,'f')
pedro.agrega_inicial(2,'g')
pedro.agrega_inicial(2,'h')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'a')

pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'b')
pedro.agrega_inicial(2,'c')
pedro.agrega_inicial(2,'d')
pedro.agrega_inicial(2,'e')
pedro.agrega_inicial(2,'f')
pedro.agrega_inicial(2,'g')
pedro.agrega_inicial(2,'h')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'i')
#pedro.agrega_inicial(2,'i')



print(pedro.tamaño)
print(pedro.ocupacion)


#print(f'tabla 2{pedro}')
pedro.prettytable(2)
"""


from nodoLL import nodito

class jacinto():
    def __init__(self):
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
    def haseho2(self,numero):
        nuevo_index = ((numero % 3)+1)*self.colisiones
        return nuevo_index

    def agrega_inicial(self,id,value):
        posicion = self.hasheo(str(id)+str(value)) % self.tamaño
        self.agregar(value,posicion)



    def agregar(self,value,index):
        k = self.head
        for n in range(index):
            k = k.Next
        if k.value == "":
            print(f'------------------------')
            print(f' ')
            print(f'[{value}] SE VA A POSICION___{index}')
            k.value = value
            self.ocupacion = self.ocupacion +1
            print(f'PORCENTAJE DE OCUPACION____{str(self.definir_porcentaje_ocupacion()*100)}...%')
            print(f'NUMERO DE COLISIONES____{str(self.colisiones)}')
            print(f' ')
            print("________________________")
        else:
            print(f'[{value}] SE HUBIERA IDO A POSICION___{index}')
            self.colisiones = self.colisiones + 1
            nuevo_index = self.haseho2(index)
            self.agregar(value, nuevo_index)
            
        
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
        
pedro = jacinto()
print(f'tabla 1{pedro}')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'a')
pedro.agrega_inicial(2,'d')
pedro.agrega_inicial(2,'e')
pedro.agrega_inicial(2,'f')
pedro.agrega_inicial(2,'g')
pedro.agrega_inicial(2,'h')
pedro.agrega_inicial(2,'i')
pedro.agrega_inicial(2,'j')
pedro.agrega_inicial(2,'k')
pedro.agrega_inicial(2,'l')
pedro.agrega_inicial(2,'m')

print(f'tabla 2{pedro}')

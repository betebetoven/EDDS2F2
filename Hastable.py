
from nodoLL import nodito
import numpy as np
class jacinto():
    def __init__(self):
        self.head = None
        self.tamaño = 13
        self.ocupacion = 0
        for n in range(self.tamaño):
            self.inicia_tamaño()

    def inicia_tamaño(self):
        if self.head == None:
            self.head = nodito('')
        else:
            k = self.head
            while k.Next != None:
                k = k.Next  
            k.Next = nodito('')
    def hasheo(self, cadena):
        general = sum(bytearray(cadena,encoding='utf-8'))
        print(f'NUMEROHASH_____{general}')
        return general
    def agregar(self, id,value):
        posicion = self.hasheo(str(id)+str(value)) % self.tamaño
        print(f'SE VA A POSICION___{posicion}')
        k = self.head
        for n in range(posicion):
            k = k.Next
        k.value = value


    
    def __str__(self) -> str:
        general = "TABLA HASH--------"
        k = self.head
        while k!= None:
            general+=f'\n{k}'
            k = k.Next
        return general
        
pedro = jacinto()
print(f'tabla 1{pedro}')
pedro.agregar(2,'betebetoven')
pedro.agregar(2,'aba')
print(f'tabla 2{pedro}')

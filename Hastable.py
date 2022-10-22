
from tkinter import messagebox
from nodoLL import nodito
import numpy as np
class jacinto():
    def __init__(self):
        self.head = None
        self.last = None
        self.tamaño = 13
        self.ocupacion = 0
        for n in range(self.tamaño):
            self.inicia_tamaño()

    def inicia_tamaño(self):
        if self.head == None:
            self.head = nodito('')
            self.last = self.head
            self.head.Next = self.last
            self.last.Next = self.head
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
        print(f'NUMEROHASH_____{general}')
        return general
    def agregar(self, id,value):
        posicion = self.hasheo(str(id)+str(value)) % self.tamaño
        print(f'SE VA A POSICION___{posicion}')
        k = self.head
        for n in range(posicion):
            k = k.Next
        print(f'ESTE ES EL VALOR QUE SE ENCUENTRA DENTRO{k}')
        if k.value == "":
            k.value = value
            self.ocupacion = self.ocupacion +1
        else:
            #aca va la resolucion de colision
            print("HUBO OCOLISIOIN")
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
pedro.agregar(2,'betebetoven')
pedro.agregar(2,'aba')
pedro.agregar(2,'cerro')
print(f'tabla 2{pedro}')

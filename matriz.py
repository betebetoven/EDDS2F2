from ast import Return
from pkgutil import ImpImporter
from tkinter.messagebox import NO
from nodo import nodo
import random 
class par:
    x = 0
    y=0
    def __init__(self,x,y ):
        self.x = x
        self.y = y
    def __str__ (self):
        return '[x:' + str(self.x) + ',y:' + str(self.y)+']'

class matriz:
    raiz = nodo("root", -1,-1)
    dx = 0
    dy = 0
    ocupados = []
    espacios = {
        "pt":4,
        "sub":3,
        "dt":2,
        "b":1
    }


   
    def __init__(self,t ):
        self.dx = t
        self.dy = t
        self.creatodo()
        

    def recursivx(self,rooot, cont, meta):
        if cont == meta:
            print(str(rooot))
            return
        else:
            rooot.derecha = nodo("ejex",cont,-1)
            rooot.derecha.izquierda = rooot
            cont = cont+1
            print(str(rooot))
            self.recursivx(rooot.derecha,cont,meta)
    
    def recursivy(self,rooot, cont, meta):
        if cont == meta:
            print(str(rooot))
            return
        else:
            rooot.abajo = nodo("ejey",-1,cont)
            rooot.abajo.arriba = rooot
            cont = cont +1
            print(str(rooot))
            self.recursivy(rooot.abajo,cont,meta )
    def creatodo(self):
        self.recursivx(self.raiz,0,self.dx)
        self.recursivy(self.raiz,0,self.dy)

    
    def ingresar(self,x,y,barco):
        for n in self.ocupados:
            if(n.x == x and n.y == y):
                return False
        if(x>=self.dx or y >= self.dy or x<0 or y < 0):
            return False
        nuevo_nodo = nodo(barco,x,y)
        ahora = self.raiz
        while(ahora.c.x != x):
            
            ahora = ahora.derecha
        
        while(ahora != None):
            
            if(ahora.abajo == None and ahora.c.y < y):
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                
            elif(ahora.abajo!= None and ahora.abajo.c.y >y and ahora.c.y < y):
                aux = ahora.abajo
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                ahora.abajo.abajo = aux
                ahora.abajo.abajo.arriba = ahora.abajo
            ahora = ahora.abajo
        ahora = self.raiz
        #ahora toca de lado de y para ingresar en x 
        while(ahora.c.y != y):
            
            ahora = ahora.abajo
        
        while(ahora != None):
            if(ahora.derecha == None and ahora.c.x < x):
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
                self.ocupados.append(par(x,y))
                return True
            elif(ahora.derecha!= None and ahora.derecha.c.x >x and ahora.c.x < x):
                aux = ahora.derecha
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
                ahora.derecha.derecha = aux
                ahora.derecha.derecha.izquierda = ahora.derecha
                self.ocupados.append(par(x,y))
                return True
            ahora = ahora.derecha
    def eliminar(self,x,y):
        if(x>self.dx or y> self.dy):
            return False                #SOLO SE UTILIZAN DOS CASOS EN LA ELIMINACION YA QUE DE FIJO 
        bandera = False    #SIEMPRE VA A TENER NODO A LA IZQUIERDA Y ARRIBA, POR LO QEU PUEDE FACTORIZARSE
        for n in self.ocupados:#A UN CASO GENERAL
            if(n.x == x and n.y == y):
                bandera = True
        if bandera == True:
            ahora = self.raiz
            while(ahora.c.x != x):
                ahora = ahora.derecha
            while(ahora.c.y != y):
                ahora = ahora.abajo
            ahora.arriba.abajo = ahora.abajo
            if(ahora.abajo != None):
                ahora.abajo.arriba = ahora.arriba
            ahora.izquierda.derecha = ahora.derecha
            if(ahora.derecha != None):
                ahora.derecha.izquierda = ahora.izquierda
            ahora= None
            for n in self.ocupados:
                if(n.x == x and n.y == y):
                    self.ocupados.remove(n)
        return bandera


    def var(self,x,y,B):
        p = range(y,y+self.espacios[B])
        for ny in p:
            if(not(self.ingresar(x,ny,B))):
                p2 = range(y,ny-1)
                for eny in p2:
                    self.eliminar(x,eny)#ESTA CONFUNCIENDO EL FALSE DE SALIDA PQ TAMBIEN BORRA EL NODO QUE YA SE ENCONTRABA AHI
                return False
        return True
    def vab(self,x,y,B):
        p = range(y+1-self.espacios[B],y+1)
        for ny in p:
            if(not(self.ingresar(x,ny,B))):
                p2 = range(y+1-self.espacios[B],ny-1)
                for eny in p2:
                    self.eliminar(x,eny)
                return False
        return True
    def vder(self,x,y,B):
        p = range(x,x+self.espacios[B])
        for ny in p:
            if(not(self.ingresar(ny,y,B))):
                p2 = range(x,ny-1)
                for eny in p2:
                    self.eliminar(eny,y)
                return False
        return True
    def viz(self,x,y,B):
        p = range(x+1-self.espacios[B],x+1)
        for ny in p:
            if(not(self.ingresar(ny,y,B))):
                p2 = range(x+1-self.espacios[B],ny-1)
                for eny in p2:
                    self.eliminar(eny,y)
                return False
        return True




    def llenadoautom(self,x,y,b):
        if self.var(x,y,b):
            print("lo hizo arriba")
        elif self.vab(x,y,b):
            print("lo hizo abajo")
        elif self.vder(x,y,b):
            print("lo hizo derecha")
        elif self.viz(x,y,b):
            print("lo hizo izquierda")
        else:
            self.llenadoautom(random.randint(0,self.dx-1),random.randint(0,self.dy-1),b)
            


        




            

    def impder(self, n):
        while(n != None):
            print(str(n),end = ' ')
            n = n.derecha

    def imprime(self, n):
        while(n!=None):
            print("FILA: ",end = ' ')
            self.impder(n)
            print("\n")
            n = n.abajo
    def muestra(self):
        self.imprime(self.raiz)

    def impderc(self, n):
        while(n != None):
            print('['+ str(n.c)+']',end = ' ')
            n = n.derecha
    def imprimec(self, n):
        while(n!=None):
            print("FILA: ",end = ' ')
            self.impderc(n)
            print("\n")
            n = n.abajo
    def muestrac(self):
        print("----------------------------------------------")
        self.imprimec(self.raiz)
        print("----------------------------------------------")
    
    ##def ingresarvertical():


    #def ingresarhorzontal():

 
        


   
 

            
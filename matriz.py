from pkgutil import ImpImporter
from tkinter.messagebox import NO
from nodo import nodo


class matriz:
    raiz = nodo("root", -1,-1)
    dx = 0
    dy = 0
   
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
        nuevo_nodo = nodo(barco,x,y)
        ahora = self.raiz
        while(ahora.c.x != x):
            print("ingreso2"+str(ahora))
            ahora = ahora.derecha
        print("se coloca y avanza"+str(ahora))
        while(ahora != None):
            print("ahora vale"+str(ahora))
            if(ahora.abajo == None and ahora.c.y < y):
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                print("si lo ingreso")
            elif(ahora.abajo!= None and ahora.abajo.c.y >y and ahora.c.y < y):
                aux = ahora.abajo
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                ahora.abajo.abajo = aux
                ahora.abajo.abajo.arriba = ahora.abajo
            ahora = ahora.abajo
        ahora = self.raiz
        while(ahora.c.y != y):
            print("ingreso2"+str(ahora))
            ahora = ahora.abajo
        print("se coloca y avanza"+str(ahora))
        while(ahora != None):
            if(ahora.derecha == None and ahora.c.x < x):
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
            elif(ahora.derecha!= None and ahora.derecha.c.x >x and ahora.c.x < x):
                aux = ahora.derecha
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
                ahora.derecha.derecha = aux
                ahora.derecha.derecha.izquierda = ahora.derecha
            ahora = ahora.derecha




            

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
        
    ##def ingresarvertical():


    #def ingresarhorzontal():

 
        


   
 

            
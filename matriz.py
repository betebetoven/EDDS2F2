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
            cont = cont+1
            print(str(rooot))
            self.recursivx(rooot.derecha,cont,meta)
    
    def recursivy(self,rooot, cont, meta):
        if cont == meta:
            print(str(rooot))
            return
        else:
            rooot.abajo = nodo("ejey",-1,cont)
            cont = cont +1
            print(str(rooot))
            self.recursivy(rooot.abajo,cont,meta )
    def creatodo(self):
        self.recursivx(self.raiz,0,self.dx)
        self.recursivy(self.raiz,0,self.dy)

    def ingresar(self,x,y,barco):
        #primero en el eje y ubicandons en el eje x
        nuevo_nodo = nodo(barco,x,y)
        ahora = self.raiz
        while(ahora.c.x != x):
            ahora = ahora.derecha
        if(ahora.abajo == None):
            ahora.abajo = nuevo_nodo
            ahora.abajo.arriba = ahora
        else:
            while(not(y<ahora.c.y and y>ahora.arriba.c.y)):
                ahora = ahora.abajo
            aptaux = ahora
            ahora.arriba.abajo = nuevo_nodo
            ahora.arriba.abajo.arriba = ahora.arriba
            ahora.arriba.abajo.abajo = aptaux
            ahora.arriba.abajo.abajo.arriba = ahora.arriba.abajo
        #ahora toca en el eje x ubicandonos en el eje y
        ahora = self.raiz
        while(ahora.c.x != x):
            ahora = ahora.derecha
        if(ahora.derecha == None):
            ahora.derecha = nuevo_nodo
            ahora.derecha.izquierda = ahora
        else:
            while(not(y<ahora.c.y and y>ahora.izquierda.c.y)):
                ahora = ahora.derecha
            aptaux = ahora
            ahora.izquierda.derecha = nuevo_nodo
            ahora.izquierda.derecha.izquierda = ahora.izquierda
            ahora.izquierda.derecha.derecha = aptaux
            ahora.izquierda.derecha.derecha.izquierda = ahora.izquierda.derecha


            



    def ingresarvertical():


    def ingresarhorzontal():

 
        


   
 

            
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

 
        


   
 

            

from tkinter import messagebox
from nodoLL import nodito
import os
class listaenlazada:
    head = None
    tamaño = 0
    general = ""
    def __init__(self):
        self.head = None
        self.tamaño = 0
        self.general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = square]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"
    def agrega(self, x,y):
        if self.head == None:
            self.head = nodito(x)
            self.head.agragaderecha(y)
            return True
        if self.contains(x,y):
            print("si lo agrego")
            return True



    def contains(self, x,y):
        aux = self.head
        while aux != None:
            if aux.value == x:
                aux.agragaderecha(y)
                return True
            if aux.Next == None:
                aux.Next = nodito(x)
                aux.Next.agragaderecha(y)
                return True
            aux = aux.Next
        return False

    def graphvix(self,a):
        self.general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = square]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"
        self.numera()
        self.conexiones()
        self.rank()
        self.general+="\n }"
        messagebox.showerror("entra?",self.general)
        f = open(f'{a}.dot', "w")
        f.write(self.general)
        f.close()
        os.system(f'dot -Tpng {a}.dot -o {a}.png')
        self.general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = square]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"
        aux = self.head
        while aux!=None:
            aux2 = aux
            while aux2.Der != None:
                self.general+=f'\n{str(aux.value)}->{str(aux2.Der.value)}'
                aux2 = aux2.Der
            aux = aux.Next
        self.general+="}"
        fx = open(f'SUB_{a}.dot', "w")
        fx.write(self.general)
        fx.close()
        os.system(f'dot -Tpng SUB_{a}.dot -o SUB_{a}.png')






    def numera(self):
        aux = self.head
        while aux != None:
            self.general += str(aux)
            aux2 = aux.Der 
            while aux2 != None:
                self.general += str(aux2)
                aux2 = aux2.Der
            aux = aux.Next
    def conexiones(self):
        aux = self.head
        while aux != None:
            if aux.Next != None:
                self.general += f'\n{str(id(aux))}-> {str(id(aux.Next))}'
            aux2 = aux
            while aux2 != None:
                if aux2.Der != None:
                    self.general += f'\n{str(id(aux2))}-> {str(id(aux2.Der))}'
                aux2 = aux2.Der
            aux = aux.Next
    def rank(self):
        n = self.head
        while n!=None:
            p=n
            self.general+="\n {rank=same; "
            while p!=None:
                self.general+=str(id(p))+";"
                p=p.Der
            n=n.Next
            self.general+="}"
    
        
        
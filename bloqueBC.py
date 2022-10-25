from datetime import datetime

from sha256 import shasha
from merkletree import MLKjunior
from LL import listaenlazada
import os
import json

class bloque:
    def __init__(self, index,transactions, prev,root):
        self.next = None
        self.index = index
        self.hash = None
        self.transactions = transactions
        self.timestamp = datetime.now().strftime("%d-%m-%Y::%H:%M:%S")
        self.prev = prev
        self.nonce = 0
        self.rootmerkle = root

    def work_hash(self,proof):
        pedro = shasha()
        #SHA256(INDEX+TIMESTAMP+PREVIOUSHASH+ROOTMERKLE+NONCE)
        sha = ""
        while True:
            sha = pedro.generate_hash(f'{str(self.index)}{str(self.timestamp)}{str(self.prev)}{str(self.rootmerkle.value)}{str(self.nonce)}').hex()
            #print(sha)
            if str(sha).startswith(proof):
                self.hash = str(sha)
                return str(sha)
                break
            self.nonce = self.nonce +1
        

    #sera que si funciona sin login   
    #ENTRA UNA LISTA ENLAZADA PARA LAS TRANSACCIONES QUE VIENE DE LA LISTA HASH. ALVVVVVVVVVVVVVVVVVVVVVVVO PUEDE SE QUE ENTRE LA LISTA HASH, UNA DE DOS
    def transacciones_a_list(self):
        general = []
        print("estas son las transacciones___")
        
        print(self.transactions.tamaño)
        if self.transactions.tamaño == 0:
            return []
        k = self.transactions.head
        while k!= None:
            print(k.value)
            general.append(k.value)
            k = k.Next
        return general
        
    def make_json(self):
        estring = str(self)
        json_object = json.dumps(estring, indent = 4) 
        print(json_object)

        

    def __str__(self):
        bloque= {
            'index' : self.index,
            'timestamp': self.timestamp,
            'nonce':self.nonce,
            'data':{
                'hash_prev':self.prev,
                'merkle_root':str(self.rootmerkle.value),
                'self_hash':self.hash,
                'transacciones':self.transacciones_a_list()
            }
        }
        
        with open(f'archivo_{self.index}.json', "w") as outfile:
            json.dump(bloque, outfile)
        
        
        #print(json_object)
        return str(bloque)

"""
prueba = listaenlazada()
prueba.agrega_simple("compra1")
prueba.agrega_simple("compra2")
prueba.agrega_simple("compra3")
t = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]

mk = MLKjunior()
nodo = mk.merkle(t)
bprueba = bloque(0,prueba,"hashprev",nodo)
bprueba.work_hash('000')
print(bprueba)
"""
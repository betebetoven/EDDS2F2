from datetime import datetime
from os import pread
from formatter import NullFormatter
from sha256 import shasha


class bloque:
    def __init__(self, index,transactions, prev,root) -> None:
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
            sha = pedro.generate_hash(f'{str(self.index)}{str(self.timestamp)}{str(self.prev)}{str()<self.rootmerkle}{str(self.rootmerkle)}')
            if sha.startswith(proof):
                self.hash = sha
                return sha
            self.nonce = self.nonce +1
        

    #sera que si funciona sin login   
    #ENTRA UNA LISTA ENLAZADA PARA LAS TRANSACCIONES QUE VIENE DE LA LISTA HASH. ALVVVVVVVVVVVVVVVVVVVVVVVO PUEDE SE QUE ENTRE LA LISTA HASH, UNA DE DOS
    def transacciones_a_list(self):
        general = []
        if len(self.transactions)== 0:
            return []
        k = self.transactions.Head
        while k!= None:
            general.append(str(k))
            k = k.next
        

            



    def __str__(self):
        self.bloque= {
            'index' : self.index,
            'timestamp': self.timestamp,
            'nonce':self.nonce,
            'data':{
                'hash_prev':self.prev,
                'merkle_root':self.rootmerkle,
                'self_hash':self.hash,
                'transacciones':self.transacciones_a_list()
            }




        }

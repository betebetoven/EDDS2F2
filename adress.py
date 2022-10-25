
from mimetypes import init
from eth_account import Account
import secrets
class direccion_from:
        
    def __init__(self):
        priv = secrets.token_hex(32)
        self.private_key = "0x" + priv
        print("SAVE BUT DO NOT SHARE THIS: ",self.private_key)
        self.acct = Account.from_key(self.private_key)
        print(f'Adress: {self.acct.address}') 
        self.dir = str(self.acct.address)
        print(self.dir)
    def new(self):
        priv = secrets.token_hex(32)
        self.private_key = "0x" + priv
        print("SAVE BUT DO NOT SHARE THIS: ",self.private_key)
        self.acct = Account.from_key(self.private_key)
        print(f'Adress: {self.acct.address}') 
        self.dir = str(self.acct.address)
        print(self.dir)
    def __str__(self) -> str:
        sh = self.dir
        return sh
    def getPriv(self):
        return str(self.private_key)


pedro = direccion_from()
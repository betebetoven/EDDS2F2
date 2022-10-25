from select import select
from sha256 import shasha
class trans:
    def __init__(self,From,Array_skins,total):
        self.From = From
        self.Array_skins = Array_skins
        self.total = total
    def sha(self):
        pedro = shasha()
        skinis = ""
        for n in self.Array_skins:
            skinis+=str(n)

        sha = pedro.generate_hash(f'{str(self.From)}{str(skinis)}').hex()
        return str(sha)
    def todict(self):
        new_arr = []
        for n in self.Array_skins:
            new_arr.append(str(n))
        data ={"from": self.From,
                "skins":new_arr,
                "total": self.total
        }
        return data
    def __str__(self) -> str:
        return str(self.todict())
    

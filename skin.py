

from Hastable import jacinto
class skin:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return self.nombre
pedro = jacinto()
skin1 = skin("betebetoven",2)
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("bete",2))
pedro.agrega_inicial(2,skin("betebeto",2))
pedro.agrega_inicial(2,skin("ben",2))
pedro.agrega_inicial(2,skin("beteb",2))
pedro.agrega_inicial(2,skin("bete",2))
pedro.agrega_inicial(2,skin("toven",2))
pedro.agrega_inicial(2,skin("ven",2))
pedro.agrega_inicial(2,skin("et",2))
pedro.agrega_inicial(2,skin("betebetoven2",2))
pedro.agrega_inicial(2,skin("blancamagy",2))
pedro.agrega_inicial(2,skin("blancamagy2",2))
print(pedro.ocupacion)
print(pedro.tamaño)
pedro.prettytable(2)
pedro.prettytable_llenos(2)
print(pedro.total())
for n in pedro.toArray():
    print(str(n))
pedro.eliminar("betebetoven")
pedro.prettytable(2)
pedro.prettytable_llenos(2)


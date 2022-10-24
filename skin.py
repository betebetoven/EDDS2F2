

from Hastable import jacinto
class skin:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self) -> str:
        return self.nombre
pedro = jacinto()
skin1 = skin("betebetoven",2)
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("betebetoven",2))
pedro.agrega_inicial(2,skin("blancamagy",2))
pedro.agrega_inicial(2,skin("blancamagy2",2))
print(pedro.ocupacion)
print(pedro.tamaño)
pedro.prettytable(2)

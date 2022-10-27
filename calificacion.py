class cali:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.partidas_ganadas = 0
    def __str__(self) -> str:
        return f'nombre: {self.nombre}\npartidas_ganadas: {self.partidas_ganadas}'
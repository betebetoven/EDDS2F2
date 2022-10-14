from tkinter.messagebox import NO


class nodito:
    value = None
    Next = None
    Der = None
    def __init__(self, value) :
        self.value = value
        self.Next = None
        self.Der = None
    def __str__(self) :
        jesus = ""
        jesus+= f'\n{str(id(self))} [label=\"{str(self.value)}\",fillcolor =\"pink\"]'
        return jesus
    def agragaderecha(self,nuevoval):
        aux = self
        while aux.Der != None:
            aux = aux.Der
        aux.Der = nodito(nuevoval)
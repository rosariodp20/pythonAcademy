from Articolo import Articolo
from Cliente import Cliente

class Prestito:

    def __init__(self, cliente:Cliente, articolo:Articolo, dataInizioPrestito:str):
        self.cliente=cliente
        self.articolo=articolo
        self.dataInizioPrestito=dataInizioPrestito

    def durataPrestito(self):
        return self.articolo.durataPrestito()+self.cliente.bonusGiorniPrestito()
    
    


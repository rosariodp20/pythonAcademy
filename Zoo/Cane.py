from Animale import Animale

class Cane(Animale):
    
    def __init__(self, nome:str, eta:int, razza:str):
        self.razza=razza
        super().__init__(nome,eta)

    def info(self):
        return self.razza
    
    def parla(self):
        return "abbaia"
    
    def muove(self):
        return "corre"

    def mangia(self):
        return "mangia"

    def beve(self):
        return "beve"

    def getRazza(self):
        return self.razza

    def setRazza(self, eta:str):
        self.razza=razza
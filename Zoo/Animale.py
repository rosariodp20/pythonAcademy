import time

class Animale():

    def __init__(self, nome:str, eta:int):
        self.nome=nome
        self.eta=eta
    
    def info(self):
        raise NotImplementedError
    
    def parla(self):
        raise NotImplementedError
    
    def muove(self):
        raise NotImplementedError

    def mangia(self):
        raise NotImplementedError
    
    def beve(self):
        raise NotImplementedError

    def dorme(self, sec:int):
        time.sleep(sec)

    def getNome(self):
        return self.nome
    
    def setNome(self, nome:str):
        self.nome=nome

    def getEta(self):
        return self.eta

    def setEta(self, eta:str):
        self.eta=eta
class Car:

    def __init__(self, resa:float):
        self.resa=resa
        self.carburante=0
    
    def drive(self, km:int):
        self.carburante-=km*self.resa
    
    def getGas(self):
        return self.carburante

    def addGas(self, c:int):
        self.carburante+=c


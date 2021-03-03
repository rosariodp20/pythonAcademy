class CarFuel:

    def __init__(self, resa:float, tipoCarburante:str):
        self.resa=resa
        self.carburante=0
        self.tipoCarburante=tipoCarburante
    
    def drive(self, km:int):
        self.carburante-=km*self.resa
    
    def getGas(self):
        return self.carburante

    def addGas(self, c:int):
        self.carburante+=c

    def usaBenzila(self):
        if self.tipoCarburante.upper=="BENZINA":
            return True
        else:
            return False

    def usaGasolio(self):
        if self.tipoCarburante.upper=="GASOLIO":
            return True
        else:
            return False

    def getTipoCarburante(self):
        return self.tipoCarburante

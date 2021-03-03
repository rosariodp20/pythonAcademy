from Car import Car

class Distributore:

    def __init__(self, prezzoPerLitro:float):
        self.prezzoPerLitro=prezzoPerLitro
        self.deposito=0
    
    def rifornisci(self, q):
        self.deposito=+q

    def vendi(self, euro:int, car:Car):
        litriVenduti=euro/self.prezzoPerLitro
        self.deposito-=litriVenduti
        car.addGas(litriVenduti)
    
    def aggiorna(self, prezzoPerLitro):
        self.prezzoPerLitro=prezzoPerLitro
    
    def getBenzina(self):
        return self.deposito
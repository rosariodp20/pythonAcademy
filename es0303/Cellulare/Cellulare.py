class Cellulare:

    def __init__(self, carica:float=0.0, numeroChiamate:int=0):
        self.carica=carica
        self.numeroChiamate=numeroChiamate

    def ricarica(self, car:float):
        self.carica+=car

    def chiama(self, minChiamata:int):
        flag=0
        costo=20
        carica=self.carica*100
        for i in range(0,minChiamata):
            if carica>=costo:
                carica-=costo
            else:
                flag=1
        self.carica=carica/100
        if flag==1:
            print("Chiamata terminata prima! Credito esaurito")
        self.numeroChiamate+=1
    
    def numero404(self):
        return self.carica
    
    def getNumeroChiamate(self):
        return self.numeroChiamate
    
    def azzeraNumeroChiamate(self):
        self.numeroChiamate=0
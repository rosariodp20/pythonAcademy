class Lampadina:

    def __init__(self, cicli:int):
        self.stato=0
        self.cicli=cicli

    def cambiaStato(self):
        if self.stato%2==0 and self.stato<=self.cicli:
            return ("Spento")
        elif self.stato%2!=0 and self.stato<=self.cicli:
            return ("Acceso")
        else:
            return ("Rotta")

    def click(self):
        self.stato+=1

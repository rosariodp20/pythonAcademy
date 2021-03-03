from Cliente import Cliente

class Studente(Cliente):

    def __init__(self, nome:str, cognome:str, facolta:str):
        self.facolta=facolta
        super().__init__(nome, cognome)

    def bonusGiorniPrestito(self):
        return 10

    def isStudente(self):
        return True
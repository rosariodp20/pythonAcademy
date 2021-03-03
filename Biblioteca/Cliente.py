class Cliente:

    def __init__(self, nome:str, cognome:str):
        self.nome=nome
        self.cognome=cognome
    
    def bonusGiorniPrestito(self):
        return 0

    def isStudente(self):
        return False
        
class Articolo():

    def __init__(self, collocazione:str, autore:str, titolo:str, tipo:str):
        self.collocazione=collocazione
        self.titolo=titolo
        self.autore=autore
        self.tipo=tipo
        if tipo.upper()=='LIBRO':
            self.prestito=30
        elif tipo.upper()=='CD':
            self.prestito=7

    def durataPrestito(self):
        return self.prestito


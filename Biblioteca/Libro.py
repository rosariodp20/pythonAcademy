from Articolo import Articolo

class Libro(Articolo):

    def __init__(self, collocazione:str,  autore:str, titolo:str, genere:str, tipo:str):
        self.genere=genere
        super().__init__(collocazione, titolo, autore, tipo)

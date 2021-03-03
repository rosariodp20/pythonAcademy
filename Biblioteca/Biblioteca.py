from Cliente import Cliente
from Studente import Studente
from Articolo import Articolo
from Libro import Libro
from CD import CD
from Prestito import Prestito

class Biblioteca:
    
    def __init__(self, denominazione:str, luogo:str):
        self.denominazione=denominazione
        self.luogo=luogo
        self.listaClienti=[]
        self.listaArticoli=[]
        self.listaPrestiti=[]

    
    def getListaPrestiti(self):
        return self.listaPrestiti

    def getListaArticoli(self):
        return self.listaArticoli

    def getListaClienti(self):
        return self.listaClienti

    def aggiungiCliente(self, nome:str, cognome:str):
        cliente = Cliente(nome,cognome)
        self.listaClienti.append(cliente)
    
    def aggiungiStudente(self, nome:str, cognome:str, facolta:str):
        studente = Studente(nome, cognome, facolta)
        self.listaClienti.append(studente)

    def aggiungiArticolo(self, collocazione:str, autore:str, titolo:str, genere:str, tipo:str):
        if tipo.upper()=='LIBRO':
            articolo=Libro(collocazione,titolo,autore,genere,tipo)
            self.listaArticoli.append(articolo)
        elif tipo.upper()=='CD':
            articolo=CD(collocazione,titolo,autore,genere,tipo)
            self.listaArticoli.append(articolo)
        else:
            print("Tipo non supportato")

    def cercaCliente(self, nome:str, cognome:str):
        for cliente in self.listaClienti:
            if cliente.nome.upper()==nome.upper() and cliente.cognome.upper()==cognome.upper():
                return cliente
        return None

    def cercaArticolo(self, titolo:str, autore:str):
        for articolo in self.listaArticoli:
            if articolo.titolo.upper()==titolo.upper() and articolo.autore.upper()==autore.upper():
                return articolo
        return None


    def registraPrestito(self, autore:str, titolo:str, nomeCliente:str, cognomeCliente:str, dataPrestito:str):
        articolo= self.cercaArticolo(titolo, autore)
        if articolo==None:
            print("Articolo non trovato")
        else:
            cliente= self.cercaCliente(nomeCliente, cognomeCliente)
            if cliente==None:
                print("Cliente non trovato")
            else:
                self.listaPrestiti.append(Prestito(cliente, articolo, dataPrestito))
    
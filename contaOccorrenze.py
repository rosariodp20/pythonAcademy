#crea una funzione che presa in input una stringa e un carattere conti le occorrenze all'interno di essa

stringa = input("Inserisci una stringa: ")

carattere = input("Inserisci un carattere: ")

while len(carattere)!=1:
    carattere = input("Inserire un unico carattere. Inserisci un carattere: ")

print('Ci sono ' + str(stringa.count(carattere)) + ' occorrenze di \'' + carattere +'\'')
import random

numRandom = random.randint(1,1000)

numIns=int(input("Indovina a che numero sto pensando: "))
while numRandom!=numIns:
    if numRandom<numIns:
        print('Il numero inserito é piú grande di quello da indovinare')
        numIns=int(input("Riprova, indovina a che numero sto pensando: "))
    else:    
        print('Il numero inserito é piú piccolo di quello da indovinare')
        numIns=int(input("Riprova, indovina a che numero sto pensando: "))


print('Complimenti, hai indovinato il numero')
    

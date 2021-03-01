import random

#apro file da leggere
fin=open('C:/Users/rosar/Desktop/BegearPython/Programmi/a.txt')
#apro file in cui scrivere
fout=open('C:/Users/rosar/Desktop/BegearPython/Programmi/wordsChanged.txt', 'w')

paroleFile = []

#conto le parole contenute nel file
for parola in fin:
    if parola!='\n':
        paroleFile.append(parola.split())
        
for i in myList:
    seed=random.randitn(0,len(myList))

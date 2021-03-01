
import random

lettura = open('C:/Users/rosar/Desktop/BegearPython/Programmi/a.txt')
scrittura = open('C:/Users/rosar/Desktop/BegearPython/Programmi/risultato.txt',"w+")

stringa = lettura.read()
myList  = stringa.split()

for i in range(0,len(myList)):
      seed=random.randint(0, len(myList)-1)
      while myList[seed]=='+':
            seed=random.randint(0, len(myList)-1)
      scrittura.write(myList[seed]+"\n")
      myList[seed]='+'
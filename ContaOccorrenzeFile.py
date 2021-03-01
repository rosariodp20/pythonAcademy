#conta occorrenze in file
fin = open('C:/Users/rosar/Desktop/BegearPython/Programmi/occ.txt').read().upper()

d=dict()

print('Ci sono ' + str(fin.count('ROSARIO')) + ' occorrenze di Rosario')

d["Rosario"]=fin.count('ROSARIO')
d["Ciao"]=fin.count('CIAO')

print(d)
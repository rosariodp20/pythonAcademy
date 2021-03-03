def sommaNumeri(lista:list):
    somma=0
    for i in range(len(lista)):
        if  isinstance(lista[i],int) and not isinstance(lista[i], bool):
            somma+=lista[i]
    return somma

l=[1,2,"13","4","645"]
print(sommaNumeri(l))
l=[True,False,"123","75"]
print(sommaNumeri(l))
l=[1,2,3,4,5,True]
print(sommaNumeri(l))


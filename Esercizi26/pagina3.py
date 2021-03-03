def aggiungiIndice(lista:list):
    for i in range (len(lista)):
        lista[i]=lista[i]+i
    return lista

l1=[0,0,0,0,0]
l1=aggiungiIndice(l1)
print(l1)
l1=[1,2,3,4,5]
l1=aggiungiIndice(l1)
print(l1)
l1=[5,4,3,2,1]
l1=aggiungiIndice(l1)
print(l1)
def contaOccorrenze(lista:list, c):
    c=str(c)
    listaIn=[]
    for i in range(len(lista)):
        lista[i]=str(lista[i])
        if lista[i]==c:
            listaIn.append(i)
    return listaIn

l1=["a","a","b","a","b","a"]
print(contaOccorrenze(l1,"a"))
l1=[1,5,5,2,7]
print(contaOccorrenze(l1,7))
l1=[1,5,5,2,7]
print(contaOccorrenze(l1,5))
l1=[1,5,5,2,7]
print(contaOccorrenze(l1,8))
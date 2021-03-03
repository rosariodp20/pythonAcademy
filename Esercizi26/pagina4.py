def contaUpper(stringa:str):
    lista = []
    for i in range(len(stringa)):
        if stringa[i].isupper():
            lista.append(i)
    return lista

stringa='eDaBiT'
print(contaUpper(stringa))
stringa='eQuINoX'
print(contaUpper(stringa))
stringa='determinate'
print(contaUpper(stringa))
stringa='STRIKE'
print(contaUpper(stringa))
stringa='sUn'
print(contaUpper(stringa))



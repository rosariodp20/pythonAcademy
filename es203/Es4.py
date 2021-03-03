esito=0

def esamina (uno, due, tre):
    if uno < (due+tre):
        esito = (uno/(due+tre))
    else:
        esito = ((due+tre)/uno)
    return esito

print(esamina(3, 1, 2))

print(esito)
lista = []
lista.insert(0,6)
lista.insert(1,6)

lista.insert(1,4)
print(lista)
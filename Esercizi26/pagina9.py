def lunghezzaNumero(num:int):
    num=str(num)
    i=0
    for e in num:
        i+=1
    return i

print(lunghezzaNumero(10))
print(lunghezzaNumero(5000))
print(lunghezzaNumero(0))
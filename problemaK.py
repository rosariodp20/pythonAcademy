num=int(input("Inserisci un numero positivo: "))
while num<=0:
    votoScritto = int(input('Inserisci un numero positivo: '))
    
k=1
sumK=0
while sumK+k<=num:
    sumK+=k
    k+=1

print(k-1)
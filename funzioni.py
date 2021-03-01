def ilPiuGrande(a:int,b:int) -> float:
    if(a>=b):
        print('Il numero piú grande é', a)
    else:
        print('Il numero piú grande é', b)

def numeroMaggiore():
    num = int(input("Inserisci numero (premere 0 per terminare): "))
    maxN = num
    while num != 0:
        num = int(input("Inserisci prossimo numero (premere 0 per terminare): "))
        if num>maxN and num!=0:
            maxN=num
    if maxN!=0:
        print(maxN)

def sommatoria():
    num = int(input("Inserisci numero (premere 0 per terminare): "))
    somma = 0+num
    if somma==0:
        return
    else:
        while num != 0:
            num = int(input("Inserisci prossimo numero (premere 0 per terminare): "))
            somma+= num
    print(somma)

def lunghezza(stringa):
    cont=0
    for c in stringa:
        if c!=" ":
            cont+=1
    print(cont)

def ordinaParola(a,b):
    if a<b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

    
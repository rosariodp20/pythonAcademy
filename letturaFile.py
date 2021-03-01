def invertiParola(parola):
    parola=parola[::-1]
    return parola

def isPalindroma(parola):
    if len(parola)%2==0:
        p1=parola[0:int(len(parola)/2)]
        p2=invertiParola(parola[(int(len(parola)/2)):int(len(parola))])
        if  p1==p2:
            return True
        else:
            return False    
    else:
        p1=parola[0:int(round(len(parola)/2),1)]
        p2=invertiParola(parola[(int(round(len(parola)/2),1)+1):int(len(parola))])
        if  p1==p2:
            return True
        else:
            return False



fil = open('C:/Users/rosar/Desktop/BegearPython/Programmi/words.txt')

for parola in fil:
        parola=parola.strip()
        if isPalindroma(parola):
            print(parola)

        






def contaDigits(stringa):
    cont=0
    for i in range(len(stringa)):    
        if stringa[i].isdigit():
            cont+=1
    return cont

def contaLettere(stringa):
    cont=0
    for i in range(len(stringa)):    
        if stringa[i].isalpha():
            cont+=1
    return cont


stringa = input("Inserisci una frase: ")
print("Ci sono",contaDigits(stringa),"digits.")
print("Ci sono",contaLettere(stringa),"lettere.")
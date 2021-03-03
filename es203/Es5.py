voto = int(input("Inserire voto (0 a 5): "))

while voto<0 or voto>5:
    voto = int(input("Errore. Inserire voto (0 a 5): "))

if voto>5: 
    print("Promosso")
elif voto == 5:
    print("Rimandato")
elif voto<5 and voto>2:
    print("Bocciato")
elif voto<=2:
    print("Espulso")
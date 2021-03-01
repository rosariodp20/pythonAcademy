num = int(input("Inserisci numero (premere 0 per terminare): "))

stampaFinale=""

if num == 0:
    print("Programma terminato")
else:
    for i in range (num):
        stampaFinale +="*"
    stampaFinale +="\n\r"

while num != 0:
    num = int(input("Inserisci prossimo numero (premere 0 per terminare): "))
    if num!= 0 :
        for i in range (num):
            stampaFinale +="*"
        stampaFinale +="\n\r"
print(stampaFinale)  
       
            
quantiNumeri = input("Quanti numeri vuoi inserire: ")
flag=0

for i in range(int(quantiNumeri)):
    num = input("Inserisci numero: ")
    num=int(num)
    print(num%2)

    if num%2!=0 or num<=0 :
        print('prova',num)
        flag=1


if flag==1:
    print('NO!')
else:
    print('Tutti positivi e pari')
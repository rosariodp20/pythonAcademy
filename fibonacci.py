num = input("Quanti numeri vuoi:\n")

num=int(num)
n1=0
n2=1
iterazioni=0

if num<=0:
    print('Inserire numero positivo maggiore di zero\n')
elif num==1:
    print('Serie di Fibonacci:\n')
    print(n1)
else:
    print('Serie di Fibonacci:\n')
    while iterazioni < num:
        print(''+str(n1)+'\n')
        tmp=n1+n2
        n1=n2
        n2=tmp
        iterazioni += 1

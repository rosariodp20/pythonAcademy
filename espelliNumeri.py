import random


list=[1,2,3]
copy=list.copy()
t = input("Vuoi un numero? ")
while 0<1:
    while t!='1' and len(list)>0:
        ran=random.randint(0, len(list)-1)
        print(list[ran])
        list.pop(ran)
        t = input("Vuoi un numero? ")
    list=copy.copy()    


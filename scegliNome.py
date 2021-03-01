import random

diz={"Marius":3, "Emilio":3, "Rosario":3}
diz2=diz.copy()
t = input("Premi invio per un nuovo nome: ")
l=len(diz)-1

f=0

while 0<1:
    while len(diz)>0:
        ran=random.randint(0, l)
        print(ran)
        if ran==0:
            if "Marius" in diz:
                if diz["Marius"]!=0:               
                    diz["Marius"]-=1
                    print('Marius con '+ str(diz["Marius"])) 
                    f=1
                elif diz["Marius"]==0:
                    del diz["Marius"]
                    f=1
            else:
                print("a")
                break
        elif ran==1:
            if "Emilio" in diz:
                if diz["Emilio"]!=0:                      
                    diz["Emilio"]-=1
                    print('Emilio con '+ str(diz["Emilio"]))
                    f=1
                elif diz["Emilio"]==0:
                    del diz["Emilio"]
                    f=1
            else:
                print("b")
                break
        elif ran==2:
            if "Rosario" in diz:
                if diz["Rosario"]!=0:
                    diz["Rosario"]-=1
                    print('Rosario con '+ str(diz["Rosario"]))
                    f=1
                elif diz["Rosario"]==0:
                    del diz["Rosario"]
                    f=1
            else:
                print("c")
                break
        if f==1:    
            f=0
            t = input("Premi invio per un nuovo nome: ")
    diz=diz2.copy()    


print(len(diz))

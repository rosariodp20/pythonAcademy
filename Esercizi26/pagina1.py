def ritornaOnline(lista:list):
    if len(lista)==0 :
        print("no one online")
    elif len(lista)==1 :
        print(lista[0], "online")
    elif len(lista)==2 :
        print(lista[0],"and",lista[1],"online")
    else:
        print(lista[0],"and",lista[1],"and", (len(lista)-2) ,"online")

l=[]
ritornaOnline(l)
l=['a']
ritornaOnline(l)
l1=["a","b"]
ritornaOnline(l1)
l2=["a","b","c"]
ritornaOnline(l2)
l3=["a","b","c","d"]
ritornaOnline(l3)
l4=["a","b","c","d","e"]
ritornaOnline(l4)
l5=["a","b","c","d","e","f"]
ritornaOnline(l5)
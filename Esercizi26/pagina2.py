def trovaMancante(lista:list):
    miss=0
    for i in range(0,10):
        if(lista.count(i+1)==0):
            miss=i+1
    return miss

ln1=[1,2,3,4,6,7,8,9,10]
print("", trovaMancante(ln1))
ln1=[7,2,3,6,5,9,1,4,8]
print("", trovaMancante(ln1))
ln1=[10,5,1,2,4,6,8,3,9]
print("", trovaMancante(ln1))


from math import factorial

def triangoloPascal(num:int):
    l = []
    for i in range (num):
        for j in range (i+1):
            l.append(factorial(i)//(factorial(j)*factorial(i-j)))
    print(l)  

triangoloPascal(1)
triangoloPascal(2)
triangoloPascal(4)
import numpy as np

def combinazioni(*args):
    prod=1
    for i in range(len(args)):
        prod*=args[i]
    return prod


print(combinazioni(2,3))
print(combinazioni(3,7,4))
print(combinazioni(2,3,4,5))
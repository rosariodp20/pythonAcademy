import numpy as np

d1=np.array((1,2,3,4,6,7))
d2=np.array((1,2,3,4))

if len(d1)>=len(d2):
    l=len(d1)
    l2=len(d2)
else:
    l=len(d2)
    l2=len(d1)

d3= list(range(0,l))


for i in range(0,l):
    if i<l2:
        d3[i]=d2[i]+d1[i]
    else:
        if len(d1)>=len(d2):
            d3[i]=d1[i]
        else:
            d3[i]=d2[i]

print(d3)
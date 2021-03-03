from Punto3D import Punto3D
from Segmento3D import Segmento3D

punto=Punto3D(2,3,4)
p2=Punto3D(1,2,3)
print(punto)
print(p2)

l=Segmento3D(punto,p2)
l2=Segmento3D()

print(l.__eq__(l))
print(l.__eq__(l2))


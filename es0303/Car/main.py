from Car import Car
from Distributore import Distributore

ClioIV=Car(1)
Q8=Distributore(1)
ClioIV.drive(1)
Q8.vendi(1, ClioIV)
print(ClioIV.getGas())

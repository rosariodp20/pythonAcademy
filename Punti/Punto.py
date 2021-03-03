import math
class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y
        

    def distanza(self, punto:Punto):
        a=(punto.x-self.x)**2
        b=(punto.y-self.y)**2
        return math.sqrt(a-b)
from Punto3D import Punto3D
import math

class Segmento3D:

    def __init__(self, pointA:Punto3D=Punto3D(0,0,0), pointB:Punto3D=Punto3D(1,1,1)):
        self.pointA=pointA
        self.pointB=pointB

    def lenght(self):
        x=(self.pointA.x-self.pointB.x)**2
        y=(self.pointA.y-self.pointB.y)**2
        z=(self.pointA.z-self.pointB.z)**2
        return  math.sqrt(x+y+z)
    
    def __eq__(self, segment:Punto3D):
        if self.pointA.x==segment.pointA.x:
            if self.pointA.y==segment.pointA.y:
                if self.pointA.z==segment.pointA.z:
                    if self.pointB.x==segment.pointB.x:
                        if self.pointB.y==segment.pointB.y:
                            if self.pointB.z==segment.pointB.z:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


        
    
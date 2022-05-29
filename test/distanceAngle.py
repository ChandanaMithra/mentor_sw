import math
from math import atan2
def getDistanceAngle(sourceX1,sourceY1,destX2,destY2):
    underRoot= ((destX2-sourceX1)**2) + ((destY2-sourceY1)**2)
    distInMeters= math.sqrt(underRoot)
    dist= int(39.37*distInMeters)
    Ax,Ay= destX2-sourceX1, destY2-sourceY1
    angleInRad= math.atan2(Ay,Ax)
    angleInDeg= int(57.2958*angleInRad)
    return dist,angleInDeg
getDistanceAngle(1,1,2,2)

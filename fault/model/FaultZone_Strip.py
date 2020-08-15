import random
import math
import sys
import numpy as np
from auxilliary.Point import Point


class FaultZone_Strip:
    # OWN:
    # inputDomain
    # edge
    # aboveLineDelta
    # belowLineDelta
    # ratio
    def __init__(self, boundary, area, rate=0.9):
        self.inputDomain = boundary
        theta = area
        self.edge = self.inputDomain[0][1] - self.inputDomain[0][0]
        lineLocation = random.randint(0, 2)  # Produces random numbers to determine where segments are generated
        p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y = 0, 0, 0, 0, 0, 0, 0, 0
        if lineLocation == 0:
            while True:
                p1x = -5000
                p2x = -5000
                p2y = -5000 + (10000 * rate * random.random())
                p3y = 5000
                p4x = (-5000 + (10000 * (1 - rate))) + (10000 * rate * random.random())
                p4y = 5000
                bigTriangleArea = (5000 - p2y) * (p4x + 5000) / 2
                self.ratio = (p4y - p2y) / (p4x - p2x)
                temp = 2 * (bigTriangleArea - 10000 * 10000 * area) / self.ratio
                if temp <= 0:    # Because the square root of negative number will cause an error
                    continue
                p3x = math.sqrt(temp) - 5000
                p1y = 5000 - self.ratio * (p3x + 5000)
                if (p3x >= (-5000 + (10000 * (1 - rate)))) and (p1y <= (-5000 + 10000 * rate)):
                    break
        elif lineLocation == 1:
            while True:
                p1x = -5000
                p2x = -5000
                p2y = -5000 + (10000 * random.random())
                p3x = 5000
                p4x = 5000
                p4y = (-5000 + (10000 * random.random()))
                p1y = p2y + 10000 * theta
                p3y = p4y + 10000 * theta
                self.ratio = (p4y - p2y) / (p4x - p2x)
                if p1y <= 5000 and p3y <= 5000:
                    break
        else:
            while True:
                p1x = -5000
                p1y = (-5000 + (10000 * (1 - rate))) + (10000 * rate * random.random())
                p2x = -5000
                p3x = (-5000 + (10000 * (1 - rate))) + (10000 * rate * random.random())
                p3y = -5000
                p4y = -5000
                self.ratio = (p3y - p1y) / (p3x - p1x)
                bigTriangleArea = (p1y + 5000) * (p3x + 5000) / 2
                temp = 2 * (10000 * 10000 * area - bigTriangleArea) / self.ratio
                if temp <= 0:    # Because the square root of negative number will cause an error
                    continue
                p4x = math.sqrt(temp) - 5000
                p2y = -self.ratio * (p4x + 5000) - 5000
                if (p4x >= (-5000 + (10000 * (1 - rate)))) and (p2y >= (-5000 + (10000 * (1 - rate)))):
                    break
        self.aboveLineDelta = p1y - self.ratio * p1x
        self.belowLineDelta = p4y - self.ratio * p4x

    def findTarget(self, p):
        if isinstance(p, Point):
            if self.belowLineDelta <= p.coordPoint[1] - self.ratio * p.coordPoint[0] <= self.aboveLineDelta:
                return True
            else:
                return False
        elif isinstance(p, np.ndarray):
            if self.belowLineDelta <= p[1] - self.ratio * p[0] <= self.aboveLineDelta:
                return True
            else:
                return False
        else:
            print("arguments mismatch in strip failure pattern")


if __name__ == '__main__':
    bd = [(-5000, 5000), (-5000, 5000)]
    area = 0.05
    for i in range(10000):
        xyz = FaultZone_Strip(bd, area, rate=0.9)
        pt = Point.generateRandP(bd)
        resp = xyz.findTarget(pt)
        print(resp)
        a = 10
        xyz.findTarget(a)

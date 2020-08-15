import math
import random

from auxilliary.Point import Point
import numpy as np


class FaultZone_Block:
    def __init__(self, boundary, area):
        self.inputDomain = boundary
        n = len(boundary)
        theta = area
        sum = 1

        for parameter in self.inputDomain:
            sum = sum * (parameter[1] - parameter[0])

        self.delta = math.pow(sum * theta, 1.0 / n)
        self.faultPoint = Point(n)

        for i in range(n):
            self.faultPoint.coordPoint[i] = self.inputDomain[i][0] + (
                    (self.inputDomain[i][1] - self.inputDomain[i][0] - self.delta) * random.random())

    def findTarget(self, p):  # p can be object of Point class or a numpy ndarray
        if isinstance(p, Point):
            for i in range(p.n):
                if (not ((p.coordPoint[i] >= self.faultPoint.coordPoint[i]) and (
                        p.coordPoint[i] <= self.faultPoint.coordPoint[i] + self.delta))):
                    return False
            return True
        elif isinstance(p, np.ndarray):
            for i in range(len(p)):
                if not ((p[i] >= self.faultPoint.coordPoint[i]) and (
                        p[i] <= self.faultPoint.coordPoint[i] + self.delta)):
                    return False
            return True
        else:
            print("Error: arguments mismatch in `findTarget` function of block failure region class")


if __name__ == '__main__':
    bd = [(-5000, 5000), (-5000, 5000)]
    myTheta = 0.99
    xyz = FaultZone_Block(bd, myTheta)

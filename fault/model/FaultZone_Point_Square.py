import math
import random
import numpy as np

from auxilliary.Point import Point


class FaultZone_Point_Square:
    def __init__(self, boundary, area):
        self.inputDomain = boundary
        self.num = 25
        theta = area
        sum = 1.0
        n = len(boundary)
        for parameter in self.inputDomain:
            sum = sum * (parameter[1] - parameter[0])
        self.delta = math.pow(sum * theta / self.num, 1.0 / n)
        # self.faultPoint = np.array([Point(n) for _ in range(self.num)])  # list of points
        self.faultPoint = []  # list of points
        temp = 0

        while temp < self.num:
            faultTemp = Point(n)
            while True:
                for i in range(n):
                    faultTemp.coordPoint[i] = self.inputDomain[i][0] + (
                            (self.inputDomain[i][1] - self.inputDomain[i][0] - self.delta) * random.random())

                if not self.isOverlap(temp, faultTemp, self.delta):
                    break
            self.faultPoint.append(faultTemp)
            temp = temp + 1

    def isOverlap(self, gNum, p, delta):  # Point p, double delta
        if gNum == 0:
            return False
        else:
            for i in range(gNum):
                ftemp = True
                for j in range(p.n):
                    if not (abs(p.coordPoint[j] - self.faultPoint[i].coordPoint[j]) < delta):
                        ftemp = False
                        break
                if ftemp:
                    return True
            return False

    def findTarget(self, p):  # Point p
        if isinstance(p, Point):
            for i in range(self.num):
                ftemp = True
                for j in range(p.n):
                    if not (self.faultPoint[i].coordPoint[j] <= p.coordPoint[j] <= self.faultPoint[i].coordPoint[j] + self.delta):
                        ftemp = False
                        break
                if ftemp:
                    return True
            return False
        elif isinstance(p, np.ndarray):
            for i in range(self.num):
                ftemp = True
                for j in range(len(p)):
                    if not (self.faultPoint[i].coordPoint[j] <= p[j] <= self.faultPoint[i].coordPoint[j] + self.delta):
                        ftemp = False
                        break
                if ftemp:
                    return True
            return False
        else:
            print("arguments mismatch in fuction point failure pattern")


if __name__ == '__main__':
    bd = [(0, 1), (0, 1)]
    failureRate = 0.1
    pointFailureZone = FaultZone_Point_Square(bd, failureRate)
    q = Point.generateRandP(bd)
    resp = pointFailureZone.findTarget(q)
    print(resp)

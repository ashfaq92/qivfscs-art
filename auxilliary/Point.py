import numpy as np
from scipy.spatial.distance import cdist


class Point:
    def __init__(self, n):
        self.n = n  # dimensionality
        self.coordPoint = np.empty(n)

    @staticmethod
    def printPoint(p):
        print(tuple(p.coordPoint), end=",")

    @staticmethod
    def getDistance(p1, p2):
        return np.linalg.norm(p1.coordPoint - p2.coordPoint)

    @staticmethod
    def generateRandP(inputDomain):
        # myFscsFaiss = FscsFaiss(bd, randSeed)
        newPoint = Point(len(inputDomain))
        newPoint.coordPoint = np.random.uniform(*np.transpose(inputDomain)).astype('float32')
        return newPoint

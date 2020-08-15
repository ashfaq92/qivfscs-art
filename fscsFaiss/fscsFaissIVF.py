import sys
import faiss
import random
import numpy as np
from scipy.spatial.distance import cdist

# Trying to speed up FSCS using SIMD instructions and Numpy array attributes and Euclidean distance normalization
from fscsSimd.fscsSimd import FscsSimd


class FscsFaissIVF:
    def __init__(self, domain, candidates=10, seed=None, nList=100, nProbe=10, dataset=False):
        self.domain = domain
        self.d = len(self.domain)
        self.candNum = candidates
        self.k = 1  # number of nearest neighbors to search
        self.nlist = nList  # faiss parameter
        quantizer = faiss.IndexFlatL2(self.d)  # the other index
        self.faissIndex = faiss.IndexIVFFlat(quantizer, self.d, self.nlist)
        if not dataset:
            tempRandData = np.random.random((100000, self.d)).astype('float32')
        else:
            tempRandData = dataset

        self.faissIndex.train(tempRandData)
        self.faissIndex.nprobe = nProbe
        np.random.seed(seed)
        self.selected_set = []  # todo: make it numpy array

    def selectBestTc(self):
        # C = np.array([self.gen_rand_tc() for _ in range(self.candidate_num)]).astype('float32')
        # C = np.random.uniform(*np.transpose(self.domain)).astype('float32')
        C = np.random.uniform(*np.transpose(self.domain), (self.candNum, self.d)).astype(
            'float32')
        D, I = self.faissIndex.search(C, self.k)
        best_distance = np.max(D)
        cIndex = np.where(D == best_distance)
        # print(cIndex)
        return C[cIndex[0][0]]

    def testEffectiveness(self, failure_region):
        # failure region is an object of faultZones classes
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        self.faissIndex.add(initialTc)
        while True:
            tc = self.selectBestTc().reshape(1, self.d)
            self.faissIndex.add(tc)
            if failure_region.findTarget(tc[0]):
                return self.faissIndex.ntotal

    def generatePoints(self, n, debug=False):
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        self.faissIndex.add(initialTc)
        while True:
            tc = self.selectBestTc().reshape(1, self.d)
            if debug:   print(tuple(tc[0]), end=",")
            self.faissIndex.add(tc)
            if self.faissIndex.ntotal >= n:
                break


if __name__ == '__main__':
    bd = [(-5000, 5000), (-5000, 5000)]
    tcNum = 1000
    randSeed = 12345
    np.random.seed(randSeed)

    # myFscsFaiss = FscsFaissIVF(bd, randSeed)
    # myFscsFaiss.generatePoints(tcNum, debug=True)
    # print()
    # print(myFscsFaiss.faissIndex.ntotal)

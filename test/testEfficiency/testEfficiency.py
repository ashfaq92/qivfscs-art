import time

from fscs.FSCS import FSCS
from fscsFaiss.fscsFaissIVF import FscsFaissIVF
from fscsSimd.fscsSimd import FscsSimd
from fscsFaiss.fscsFaiss import FscsFaiss
from swfcArt.SwfcArt import SwfcArt


# todo: feeding random seed
# todo: making all results in one file
class TestEfficiency:
    def __init__(self, sim):
        self.simulations = sim

    def main(self):
        testCases = []
        domains = []
        # testCases.append(100)
        # testCases.append(200)
        testCases.append(500)
        # testCases.append(1000)
        # testCases.append(2000)
        testCases.append(5000)
        testCases.append(10000)
        testCases.append(15000)
        testCases.append(20000)
        bd2 = [(-5000, 5000), (-5000, 5000)]
        bd3 = [(-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd4 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd5 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd10 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000), (-5000, 5000), (-5000, 5000)]

        bd15 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000)]

        domains.append(bd2)
        # domains.append(bd3)
        # domains.append(bd4)
        domains.append(bd5)
        domains.append(bd10)
        domains.append(bd15)

        for bd in domains:
            for n in testCases:
                print('d: ', len(bd), 'tcNum', n)
                # t1 = self.testFscs(bd, n)
                # print(t1, end="\t")
                # t2 = self.testFscsSimd(bd, n)
                # print(t2, end="\t")
                t3 = self.testFscsFaiss(bd, n)
                print(t3, end="\t")
                # t4 = self.testSwfcArt(bd, n)
                # print(t4, end="\t")
                t5 = self.testFscsFaissIVF(bd, n)
                print(t5, end="\t")
                print("")

    def testFscs(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsART" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscs = FSCS(bd)
            myFscs.generatePoints(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def testFscsSimd(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsSimd" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscsSimd = FscsSimd(bd)
            myFscsSimd.generatePoints(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def testFscsFaiss(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsFaiss" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscsFaiss = FscsFaiss(bd)
            myFscsFaiss.generatePoints(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def testFscsFaissIVF(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsFaissIVF" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscsFaissIVF = FscsFaissIVF(bd)
            myFscsFaissIVF.generatePoints(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def testSwfcArt(self, bd, n):
        fileName = str(len(bd)) + "d" + "SwfcArt" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            mySwfcArt = SwfcArt(bd)
            mySwfcArt.generatePoints(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations


if __name__ == '__main__':
    simulations = 100
    xyz = TestEfficiency(simulations)
    xyz.main()

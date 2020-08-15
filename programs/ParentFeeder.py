from ctypes import *
import random
import time
import numpy as np

from fscsFaiss.fscsFaissIVF import FscsFaissIVF
from fscsFaiss.fscsFaiss import FscsFaiss


class ParentFeeder:  # <= note!
    def __init__(self, sim, progName, dom, dllP):
        self.simulations = sim
        self.programName = progName
        self.domain = dom
        self.d = len(self.domain)
        self.dllPath = dllP
        self.lib = cdll.LoadLibrary(dllP)

    def checkFailure(self, tc):  # <= Note!
        # arguments in tuple data type
        pass

    def gen_rand_tc(self):
        # print(self.domain)
        return tuple(random.uniform(coord[0], coord[1]) for coord in self.domain)

    def randomTesting(self):
        fileName = self.programName + "RT.txt"
        f = open(fileName, "a")
        fMeasure = 0
        tcGenTime = 0
        execTime = 0
        while True:
            start = time.time()
            tc = self.gen_rand_tc()
            tcGenTime = tcGenTime + (time.time() - start)

            fMeasure = fMeasure + 1

            start = time.time()
            revealFailure = self.checkFailure(tc)  # <= note!
            execTime = execTime + (time.time() - start)
            if revealFailure:
                f.write(str(fMeasure) + "\t" + str(tcGenTime) + "\t" + str(execTime) + "\n")
                f.close()
                return {"fMeasure": fMeasure, "tcGenTime": tcGenTime, "execTime": execTime}

    def fscsTesting(self):
        fileName = self.programName + "FSCS.txt"  # <= note!
        f = open(fileName, "a")
        myFscs = FscsFaiss(self.domain)
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        myFscs.faissIndex.add(initialTc)
        tcGenTime = 0
        execTime = 0
        while True:
            start = time.time()
            tc = myFscs.selectBestTc()
            tcGenTime = tcGenTime + (time.time() - start)

            myFscs.faissIndex.add(tc.reshape(1, self.d))

            start = time.time()
            revealFailure = self.checkFailure(tc)
            execTime = execTime + (time.time() - start)
            if revealFailure:
                f.write(str(myFscs.faissIndex.ntotal) + "\t" + str(tcGenTime) + "\t" + str(execTime) + "\n")
                f.close()
                return {"fMeasure": myFscs.faissIndex.ntotal, "tcGenTime": tcGenTime, "execTime": execTime}

    def qivfscsTesting(self):
        fileName = self.programName + "QIVFSCS.txt"  # <= note!
        f = open(fileName, "a")
        myQivfscs = FscsFaissIVF(self.domain)
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        myQivfscs.faissIndex.add(initialTc)
        tcGenTime = 0
        execTime = 0
        while True:
            start = time.time()
            tc = myQivfscs.selectBestTc()
            tcGenTime = tcGenTime + (time.time() - start)

            myQivfscs.faissIndex.add(tc.reshape(1, self.d))

            start = time.time()
            revealFailure = self.checkFailure(tc)
            execTime = execTime + (time.time() - start)
            if revealFailure:
                f.write(str(myQivfscs.faissIndex.ntotal) + "\t" + str(tcGenTime) + "\t" + str(execTime) + "\n")
                f.close()
                return {"fMeasure": myQivfscs.faissIndex.ntotal, "tcGenTime": tcGenTime, "execTime": execTime}

    def main(self):
        print(self.programName)
        RT_Fm, RT_tcGenTime, RT_execTime = 0, 0, 0
        FSCS_Fm, FSCS_tcGenTime, FSCS_execTime = 0, 0, 0
        QIVFSCS_Fm, QIVFSCS_tcGenTime, QIVFSCS_execTime = 0, 0, 0

        for i in range(self.simulations):
            resp = self.randomTesting()
            # print("RT", resp)
            RT_Fm = RT_Fm + resp['fMeasure']
            RT_tcGenTime = RT_tcGenTime + resp['tcGenTime']
            RT_execTime = RT_execTime + resp['execTime']

            resp = self.fscsTesting()
            # print("FSCS", resp)
            FSCS_Fm = FSCS_Fm + resp['fMeasure']
            FSCS_tcGenTime = FSCS_tcGenTime + resp['tcGenTime']
            FSCS_execTime = FSCS_execTime + resp['execTime']

            resp = self.qivfscsTesting()
            QIVFSCS_Fm = QIVFSCS_Fm + resp['fMeasure']
            QIVFSCS_tcGenTime = QIVFSCS_tcGenTime + resp['tcGenTime']
            QIVFSCS_execTime = QIVFSCS_execTime + resp['execTime']

        print("F_measure  \t  tcGenTime  \t execTime")
        print("RT:", (RT_Fm / self.simulations), "\t", (RT_tcGenTime / self.simulations), "\t",
              (RT_execTime / self.simulations))
        print("FSCS:", (FSCS_Fm / self.simulations), "\t", (FSCS_tcGenTime / self.simulations), "\t",
              (FSCS_execTime / self.simulations))
        print("QIVFFSCS:", (QIVFSCS_Fm / self.simulations), "\t", (QIVFSCS_tcGenTime / self.simulations), "\t",
              (QIVFSCS_execTime / self.simulations))

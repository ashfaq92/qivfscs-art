from fault.model import FaultZone_Point_Square, FaultZone_Strip, FaultZone_Block
from fscs.FSCS import FSCS
from fscsFaiss.fscsFaiss import FscsFaiss
from fscsFaiss.fscsFaissIVF import FscsFaissIVF
from fscsSimd.fscsSimd import FscsSimd
from swfcArt.SwfcArt import SwfcArt


class TestEffectiveness:
    def __init__(self, sim):
        self.simulations = sim

    def main(self):
        failure_rates = [0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001]
        failure_rates.reverse()
        # failure_rates = [0.0001]
        domains = []
        bd2 = [(-5000, 5000), (-5000, 5000)]
        bd3 = [(-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd4 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd5 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd10 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000), (-5000, 5000), (-5000, 5000)]

        # domains.append(bd2)
        # domains.append(bd3)
        # domains.append(bd4)
        # domains.append(bd5)
        domains.append(bd10)
        for bd in domains:
            print("\n------DIMENSION:\t", len(bd), "D--------:")
            # myFscsSimd = FscsSimd(bd)
            # fscsDataSet = myFscsSimd.generatePoints(50000, debug=False)
            for theta in failure_rates:
                print(len(bd), "D", theta)
                fileNameBlock = str(len(bd)) + "d" + "-Block-" + str(theta) + str(".txt")
                fileNameStrip = str(len(bd)) + "d" + "-Strip-" + str(theta) + str(".txt")
                fileNamePoint = str(len(bd)) + "d" + "-Point-" + str(theta) + str(".txt")
                # self.fixRateTest(theta, bd, "block", fileNameBlock)
                # self.fixRateTest(theta, bd, "strip", fileNameStrip)
                self.fixRateTest(theta, bd, "point", fileNamePoint)

    def fixRateTest(self, area, domain, fp, fileName, dataSet=False):
        failureRegion = None
        repeatFactor = 30
        total1, total2, total3, total4 = 0, 0, 0, 0
        simMin = int(self.simulations / repeatFactor)
        f = open(fileName, "w")
        for i in range(simMin):
            if fp == "block":
                failureRegion = FaultZone_Block.FaultZone_Block(domain, area)
            elif fp == "strip":
                failureRegion = FaultZone_Strip.FaultZone_Strip(domain, area)
            elif fp == "point":
                failureRegion = FaultZone_Point_Square.FaultZone_Point_Square(domain, area)
            for j in range(repeatFactor):
                # myFscsSimd = FscsSimd(domain)
                # fMeasure = myFscsSimd.testEffectiveness(failureRegion)
                # total1 = total1 + fMeasure
                # # print(fMeasure)
                # f.write(str(fMeasure) + "\t")

                # mySwfcArt = SwfcArt(domain)
                # fMeasure = mySwfcArt.testEffectiveness(failureRegion)
                # total2 = total2 + fMeasure
                # # print(fMeasure)
                # f.write(str(fMeasure) + "\t")

                # myFscsFaiss = FscsFaiss(domain)
                # fMeasure = myFscsFaiss.testEffectiveness(failureRegion)
                # total3 = total3 + fMeasure
                # # print(fMeasure)
                # f.write(str(fMeasure) + "\t")

                myFscsFaissIVF = FscsFaissIVF(domain)
                fMeasure = myFscsFaissIVF.testEffectiveness(failureRegion)
                total4 = total4 + fMeasure
                # print(fMeasure)
                print('.', end="")
                f.write(str(fMeasure) + "\t")
                f.write("\n")
            print()
        n = self.simulations
        s = 1 / area / 100
        print((total1 / n / s), "\t", (total2 / n / s), "\t", (total3 / n / s), (total4 / n / s))
        f.write(
            str(total1 / n / s) + "\t" + str(total2 / n / s) + "\t" + str(total3 / n / s) + "\t" + str(total4 / n / s))
        f.close()


if __name__ == '__main__':
    trials = 1500
    xyz = TestEffectiveness(trials)
    xyz.main()

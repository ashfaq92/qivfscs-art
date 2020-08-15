from programs.airy.AiryFeeder import AiryFeeder
from programs.bessj.bessjFeeder import BessjFeeder
from programs.bessj0.bessj0Feeder import Bessj0Feeder
from programs.cel.celFeeder import CelFeeder
from programs.el2.el2Feeder import El2Feeder
from programs.erfcc.erfccFeeder import ErfccFeeder
from programs.gammq.gammqFeeder import GammqFeeder
from programs.golden.goldenFeeder import GoldenFeeder
from programs.plgndr.plgndrFeeder import PlgndrFeeder
from programs.probks.probksFeeder import ProbksFeeder
from programs.sncndn.sncndnFeeder import SncndnFeeder
from programs.tanh.tanhFeeder import TanhFeeder

simulations = 10000

AiryFeeder(simulations).main()
BessjFeeder(simulations).main()
Bessj0Feeder(simulations).main()
CelFeeder(simulations).main()
El2Feeder(simulations).main()
ErfccFeeder(simulations).main()
GammqFeeder(simulations).main()
GoldenFeeder(simulations).main()
PlgndrFeeder(simulations).main()
ProbksFeeder(simulations).main()
SncndnFeeder(simulations).main()
TanhFeeder(simulations).main()

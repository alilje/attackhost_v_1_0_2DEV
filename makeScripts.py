import os
from gov.sandia.atomicHost.maker.makerfiles import DatDoc
from gov.sandia.atomicHost.maker.makerfiles import SupportingDirs
from gov.sandia.atomicHost.maker.makerfiles import AttackScript
from gov.sandia.atomicHost.maker.makerfiles import CleanUpScript

mm = DatDoc("data/input/maker/T1560_001_01.dat")
#s = SupportingDirs(mm)
a = AttackScript(mm)
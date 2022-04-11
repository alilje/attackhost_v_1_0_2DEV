import os
from gov.sandia.attackHost.maker.makerfiles import DatDoc
from gov.sandia.attackHost.maker.makerfiles import SupportingDirs
from gov.sandia.attackHost.maker.makerfiles import AttackScript
from gov.sandia.attackHost.maker.makerfiles import CleanUpScript

print(os.getcwd())
mm = DatDoc("data/input/maker/T1560_001_01.dat")
s = SupportingDirs(mm)
a = AttackScript(mm)
print(os.getcwd())
#E:\AttackHost\attackhost_v_1_0_2DEV\makeScripts.py
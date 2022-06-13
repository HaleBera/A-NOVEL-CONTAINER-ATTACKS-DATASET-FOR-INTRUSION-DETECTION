from attackerBase import *

# Import your custom attack classes here

from OSCI_CVE_2019_15107_Attacker1 import OSCI_CVE_2019_15107_Attacker1
from OSCI_CVE_2019_15107_Attacker2 import OSCI_CVE_2019_15107_Attacker2
from OSCI_CVE_2019_15107_Attacker3 import OSCI_CVE_2019_15107_Attacker3


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [OSCI_CVE_2019_15107_Attacker1(),\
               OSCI_CVE_2019_15107_Attacker2(), \
               OSCI_CVE_2019_15107_Attacker3()]
    # Call your custom attacks here

    tic = time.time()
    indices = [x for x in range(len(attacks))]

    while len(indices):
        i = random.randrange(len(indices))
        del indices[i]
        
        attackInvoker(attacks[i])
        time.sleep(random.randint(5,8))
        
        del attacks[i]


    toc = time.time()

    print("Total elapsed time: ", toc - tic)
    

    






from attackerBase import *

# Import your custom attack classes here

from SQLI_CVE_2020_9483_Attacker1 import SQLI_CVE_2020_9483_Attacker1
from SQLI_CVE_2020_9483_Attacker2 import SQLI_CVE_2020_9483_Attacker2
from SQLI_CVE_2020_9483_Attacker3 import SQLI_CVE_2020_9483_Attacker3


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [SQLI_CVE_2020_9483_Attacker1(),\
               SQLI_CVE_2020_9483_Attacker2(), \
               SQLI_CVE_2020_9483_Attacker3()]
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
    

    






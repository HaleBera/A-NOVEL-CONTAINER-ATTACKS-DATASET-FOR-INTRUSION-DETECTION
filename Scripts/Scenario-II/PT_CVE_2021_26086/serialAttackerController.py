from attackerBase import *

# Import your custom attack classes here

from PT_CVE_2021_26086_Attacker1 import PT_CVE_2021_26086_Attacker1
from PT_CVE_2021_26086_Attacker2 import PT_CVE_2021_26086_Attacker2
from PT_CVE_2021_26086_Attacker3 import PT_CVE_2021_26086_Attacker3


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [PT_CVE_2021_26086_Attacker1(),\
               PT_CVE_2021_26086_Attacker2,\
               PT_CVE_2021_26086_Attacker3]

    # Call your custom attacks here

    tic = time.time()

    indices = [x for x in range(len(attacks))]

    while len(indices):
            i = random.randrange(len(indices))
            del indices[i]

            attackInvoker(attacks[i])
            time.sleep(random.randint(1,4))

            del attacks[i]

    toc = time.time()

    print("Total elapsed time: ", toc - tic)
    

    







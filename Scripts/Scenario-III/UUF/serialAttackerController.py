from attackerBase import *

# Import your custom attack classes here

from UUF_CVE_2020_25213_Attacker1 import UUF_CVE_2020_25213_Attacker1
from UUF_CVE_2020_25213_Attacker2 import UUF_CVE_2020_25213_Attacker2
from UUF_CVE_2020_25213_Attacker3 import UUF_CVE_2020_25213_Attacker3
from UUF_CVE_2020_25213_Attacker4 import UUF_CVE_2020_25213_Attacker4
from UUF_CVE_2020_25213_Attacker5 import UUF_CVE_2020_25213_Attacker5
from UUF_CVE_2020_25213_Attacker6 import UUF_CVE_2020_25213_Attacker6


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [UUF_CVE_2020_25213_Attacker1(),\
               UUF_CVE_2020_25213_Attacker2(),\
               UUF_CVE_2020_25213_Attacker3(),\
               UUF_CVE_2020_25213_Attacker4(),\
               UUF_CVE_2020_25213_Attacker5(),\
               UUF_CVE_2020_25213_Attacker6()]
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
    

    






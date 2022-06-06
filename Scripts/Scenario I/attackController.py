from attackerBase import *

# Import your custom attack classes here
from UUF_CVE_2020_25213_Attacker1 import UUF_CVE_2020_25213_Attacker1

import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [UUF_CVE_2020_25213_Attacker1()]
    # Call your custom attacks here

    tic = time.time()

    for attack in attacks:
        attackInvoker(attack)
        time.sleep(random.randint(5,8))

    toc = time.time()

    print("Total elapsed time: ", toc - tic)
    

    






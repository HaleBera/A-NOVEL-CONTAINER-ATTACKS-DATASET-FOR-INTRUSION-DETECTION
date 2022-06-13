from attackerBase import *

# Import your custom attack classes here

from PT_CVE_2021_26086_Attacker3 import PT_CVE_2021_26086_Attacker3


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks = [PT_CVE_2021_26086_Attacker3()]
    # Call your custom attacks here

    tic = time.time()

    for attack in attacks:
        attackInvoker(attack)
        time.sleep(random.randint(5,8))

    toc = time.time()

    print("Total elapsed time: ", toc - tic)
    

    







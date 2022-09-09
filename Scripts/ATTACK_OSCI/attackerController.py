from attackerBase import *

# Import your custom attacker classes here
from XSS_CVE_2019_7543_Attacker1 import XSS_CVE_2019_7543_Attacker1
from XSS_CVE_2019_7543_Attacker2 import XSS_CVE_2019_7543_Attacker2
from XSS_CVE_2019_7543_Attacker3 import XSS_CVE_2019_7543_Attacker3
from XSS_CVE_2019_7543_Attacker4 import XSS_CVE_2019_7543_Attacker4
from XSS_CVE_2019_7543_Attacker5 import XSS_CVE_2019_7543_Attacker5
from XSS_CVE_2019_7543_Attacker6 import XSS_CVE_2019_7543_Attacker6


import time
import random

def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()
    print("Finished attack "+ attackerBase.__class__.__name__)

if __name__ == '__main__':
    attacks =  [XSS_CVE_2019_7543_Attacker1(),\
               XSS_CVE_2019_7543_Attacker2(),\
               XSS_CVE_2019_7543_Attacker3(),\
               XSS_CVE_2019_7543_Attacker4(),\
               XSS_CVE_2019_7543_Attacker5(),\
               XSS_CVE_2019_7543_Attacker6()]
    # Call your custom attacks here

    tic = time.time()

    for attack in attacks:
        attackInvoker(attack)
        time.sleep(random.randint(1,4))

    toc = time.time()

    print("Total elapsed time: ", toc - tic)
    

    







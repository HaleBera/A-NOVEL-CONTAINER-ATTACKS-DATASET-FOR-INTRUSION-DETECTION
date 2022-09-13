from attackerBase import *

# Import your custom attack classes here

from PT_CVE_2020_17518_Attacker1 import PT_CVE_2020_17518_Attacker1
from PT_CVE_2020_17518_Attacker2 import PT_CVE_2020_17518_Attacker2
from PT_CVE_2020_17518_Attacker3 import PT_CVE_2020_17518_Attacker3
from PT_CVE_2021_26086_Attacker1 import PT_CVE_2021_26086_Attacker1
from PT_CVE_2021_26086_Attacker2 import PT_CVE_2021_26086_Attacker2
from PT_CVE_2021_26086_Attacker3 import PT_CVE_2021_26086_Attacker3


import time
import random

def convert_time(sec):
    min= sec/60
    return min


def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()

if __name__ == '__main__':

    Round_Number = 60
    ip_addr = ''
    yaml_path = '/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION-main/Scripts/'

    tic = time.time()

    for r in range(Round_Number):
	    attacks = [PT_CVE_2020_17518_Attacker1(ip_addr, yaml_path),\
               	       PT_CVE_2020_17518_Attacker2(ip_addr, yaml_path),\
               	       PT_CVE_2020_17518_Attacker3(ip_addr, yaml_path),\
                       PT_CVE_2021_26086_Attacker1(ip_addr, yaml_path),\
                       PT_CVE_2021_26086_Attacker2(ip_addr, yaml_path),\
                       PT_CVE_2021_26086_Attacker3(ip_addr, yaml_path)]
	    indices = [x for x in range(len(attacks))]
	    print(len(indices))
	    while len(indices):
		    i = random.randrange(len(indices))
		    del indices[i]

		    attackInvoker(attacks[i])
		    time.sleep(random.randint(0,4))

		    del attacks[i]


    toc = time.time()

    print("Total elapsed time: ", toc - tic)

    m=convert_time(toc - tic)
    print("Total Minutes=",m)
    

    






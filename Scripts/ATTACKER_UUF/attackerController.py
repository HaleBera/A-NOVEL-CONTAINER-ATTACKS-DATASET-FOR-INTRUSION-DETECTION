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

    for r in range(2):
	    attacks =  [UUF_CVE_2020_25213_Attacker1(ip_addr, yaml_path),\
                        UUF_CVE_2020_25213_Attacker2(ip_addr, yaml_path),\
                        UUF_CVE_2020_25213_Attacker3(ip_addr, yaml_path),\
                        UUF_CVE_2020_25213_Attacker4(ip_addr, yaml_path),\
                        UUF_CVE_2020_25213_Attacker5(ip_addr, yaml_path),\
                        UUF_CVE_2020_25213_Attacker6(ip_addr, yaml_path)]
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
    

    






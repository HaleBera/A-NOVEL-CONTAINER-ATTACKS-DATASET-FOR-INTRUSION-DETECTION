
# A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION
!! Outputs folder is moved to : https://github.com/HaleBera/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION-Outputs

!! "Deployments", "MonitoringTcpDump"," TESTING_TEAM.ipynb" and "(NEW)Vulnerable Image List" folder is moved to: https://github.com/HaleBera/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION-Deployments


-----------------------------------------------------------------------------------------------------
WEAKNESSES & VULNERABILITIES
-----------------------------------------------------------------------------------------------------
    CWE-79:  CVE-2019-7543
    CWE-78:  CVE-2019-15107,CVE-2019-16662
    CWE-89:  CVE-2020-9483
    CWE-22:  CVE-2020-17518,CVE-2021-26086 
    CWE-434: CVE-2020-25213



-----------------------------------------------------------------------------------------------------
TESTING ENVIRONMENT
-----------------------------------------------------------------------------------------------------

    On the same host we established a kubernetes cluster with deployments in the https://github.com/HaleBera/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION-Deployments
    For virtualization we used vagrant virtual boxes with a Nuclei Engine inside, as an attacker.




-----------------------------------------------------------------------------------------------------
DATASET CREATION SCENARIOS 
-----------------------------------------------------------------------------------------------------

    SCENARIO I: "Define different Attackers for each CVE. by using different types of commands or payloads"
    -----------
        1. For each CVE, we defined at least "3" different attackers, using attackerBase.py

            - SQL_CVE_2020_9483_Attacker_I.py
            - SQL_CVE_2020_9483_Attacker_II.py
            - SQL_CVE_2020_9483_Attacker_III.py


        2. To make each attacker have a unique IP address, in different vagrants.

        SUBSCENARIO I.I:
        ----------------
            0. Perform the tests of each CVE at a time

        SUBSCENARIO I.II:
        ----------------
            0. Perform the tests of ALL CVEs at the same time









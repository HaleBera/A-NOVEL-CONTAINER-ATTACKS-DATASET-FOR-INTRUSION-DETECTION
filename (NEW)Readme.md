# A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION



-----------------------------------------------------------------------------------------------------
WEAKNESSES ------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------
    CWE-79
    CWE-78
    CWE-89
    CWE-22
    CWE-434



-----------------------------------------------------------------------------------------------------
VULNERABILITIES -------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

    CWE-79
        - CVE-2020-9496
        - CVE-2019-7543
        - (Will be find ...)
    CWE-78
        - CVE-2019-15107
        - CVE-2019-15107
        - (Will be find ...)
    CWE-89
        - CVE-2020-9483
        - CVE-2020-12720
        - CVE-2020-10546 (May replaced by another ...)
    CWE-22
        - CVE-2020-17518
        - CVE-2021-26086
        - CVE-2021-43495 (May replaced by another ...)
    CWE-434
        - CVE-2020-25213
        - CVE-2021-25281 (May replaced by another ...)
        - (Will be find ...)



-----------------------------------------------------------------------------------------------------
TESTING ENVIRONMENT ---------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

    On the same host we established a kubernetes cluster
    For virtualization we used vagrant with a Nuclei Engine, as an attacker




-----------------------------------------------------------------------------------------------------
DATASET CREATION SCENARIOS --------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

    SCENARIO I: "Define different Attackers for each CVE. Each will use different types of commands and payloads"
    -----------
        1. For each CVE, define at least "3" different attackers, using attackerBase.py (A total of "9" attackers per CWE)

            - SQL_CVE_2020_9483_Attacker_I.py
            - SQL_CVE_2020_9483_Attacker_II.py
            - SQL_CVE_2020_9483_Attacker_III.py


        2. To make each attacker have a unique IP address, create each childAttacker.py derived from the attackerBase.py, in different vagrants (A total of "9" vagrants per CWE)

        SUBSCENARIO I.I:
        ----------------
            0. Perform the tests of each CVE at a time

        SUBSCENARIO I.II:
        ----------------
            0. Perform the tests of ALL CVEs at the same time




     SCENARIO II: "Define longer attacks for each Attacker"
    -----------
        1. For each CVE, define at least "3" different attackers, using attackerBase.py, but this time define "2" other behaviours for each attacker with the same main phase of the attack (Nuclei.yaml). (Again, a total of "9" attackers per CWE, but the "3" behaviors will be called in the same "attackerController.py" ---> ofcourse deeded to be renamed SQL_CVE_2020_9483_Attacker_I_Controller.py )

            - SQL_CVE_2020_9483_Attacker_I.py (Behavior_0)
            - SQL_CVE_2020_9483_Attacker_I_Behavior_I.py
            - SQL_CVE_2020_9483_Attacker_I_Behavior_II.py

            - SQL_CVE_2020_9483_Attacker_II.py (Behavior_0)
            - SQL_CVE_2020_9483_Attacker_II_Behavior_I.py
            - SQL_CVE_2020_9483_Attacker_II_Behavior_II.py


        2. To make each attacker, not each attacker behaviour, have a unique IP address, create each childAttacker.py derived from the attackerBase.py, in diffrent vagrants (Still, a total of "9" vagrants per CWE)

        SUBSCENARIO I.I:
        ----------------
            0. Perform the tests of each CVE at a time

        SUBSCENARIO I.II:
        ----------------
            0. Perform the tests of ALL CVEs at the same time



    SCENARIO III: "Create new attacks by combining the pre &post phases of the previously defined attacks for each Attacker"
    -----------
        (Will be performed later, it needs automation)



    SCENARIO IV: "Define a serialized attack flow for each Attacker,this time by permutation of the CWEs "
    -----------
       (Will be performed later, it needs automation)



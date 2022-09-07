
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

    The vulnerable cluster and the attackers are on the same host.
    
        - A kubernetes cluster is established by using the deployments in https://github.com/yigitsever/deployments.
        - Vagrant virtual boxes are used for virtualizing the attackers.
            - A Nuclei Engine is used to implement attacks   
            
------------------------------------------------------------------------------------------------------
 


Recording

sudo tcpdump -i eno1 src ip_addres_of atacker  -vv -w .pcap_file_location






-----------------------------------------------------------------------------------------------------
WEAKNESSES & VULNERABILITIES
-----------------------------------------------------------------------------------------------------

    CWE-79  (XSS):  Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    CWE-78 (OSCI):  Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    CWE-89 (SQLI):  Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
    CWE-22   (PT):  Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    CWE-434 (UUF):  Unrestricted Upload of File with Dangerous Type
    
    ___________________________________________________________________
    CWE-ID  |   CVE-ID         |   CVSS Score          
    ___________________________________________________________________
    CWE-79  |   CVE-2019-7543  |   V3.0: 6.1 MEDIUM
            |                  |   V2.0: 4.3 MEDIUM
    ___________________________________________________________________                      
    CWE-78  |  CVE-2019-15107  |   V3.0: 9.8  CRITICAL
            |                  |   V2.0: 10.0 HIGH
            |  CVE-2019-16662  |   V3.0: 9.8  CRITICAL
            |                  |   V2.0: 10.0 HIGH          
    ___________________________________________________________________        
    CWE-89  |  CVE-2020-9483   |   V3.1: 7.5 HIGH
            |                  |   V2.0: 5.0 MEDIUM
    ___________________________________________________________________     
    CWE-22  |  CVE-2020-17518  |   V3.1: 7.5 HIGH
            |                  |   V2.0: 5.0 MEDIUM  
            |  CVE-2021-26086  |   V3.1: 5.3 MEDIUM
            |                  |   V2.0: 5.0 MEDIUM    
    ___________________________________________________________________       
    CWE-434 |  CVE-2020-25213  |   V3.1: 9.8 CRITICAL
            |                  |   V2.0: 7.5 HIGH 
       



-----------------------------------------------------------------------------------------------------
TESTING ENVIRONMENT
-----------------------------------------------------------------------------------------------------

    The vulnerable cluster and the attackers are on the same host.
    
        - A kubernetes cluster is established by using the deployments in https://github.com/yigitsever/deployments.
        - Vagrant virtual boxes are used for virtualizing the attackers.
            - A Nuclei Engine is used to implement attacks   
            


-----------------------------------------------------------------------------------------------------
MONITORING
-----------------------------------------------------------------------------------------------------
    For monitoring we used tcpdump and record .pcap files.
    Then we give the .pcap files into the CICFlowMETER to get network-flows.
    Lastly, we labeled the flow datasets and split them into train-test (66% - 33%) datesets. 





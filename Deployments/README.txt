The kubectl deployment ".yaml" files were created for each of the seven vulnerabilities and can be reached from https://github.com/yigitsever/deployments

The construced kubernetes deployment yamls and matching vulnerability information:

     CWE-79:  CVE-2019-7543  => kindeditor | vulfocus/kindeditor-cve_2018_18950:latest  | Port: 80-30002
     
     CWE-78:  CVE-2019-15107 => webmin  | vulhub/webmin:1.910                    | Port: 10000-30003
     CWE-78:  CVE-2019-16662 => rconfig | vulfocus/rconfig-cve_2019_16662:latest | Port: 8080-30004                                        
     
     CWE-89:  CVE-2020-9483  => skywalking | vulfocus/skywalking-cve_2020_9483:latest | Port: 8080-30005
     
     CWE-22:  CVE-2020-17518 => flink | vulfocus/flink-cve_2020_17519:latest | Port: 8081-30006
     CWE-22:  CVE-2021-26086 => jira | vulfocus/jira-cve_2019_8451:latest | Port: 8080-30080 
     
     CWE-434: CVE-2020-25213 => wp-file-manager | ridgesecuritydocker/cve-2020-25213:mywordpress1 | Port: 80-30007

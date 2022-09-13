# Import abstract base class library
from abc import ABC, abstractmethod
from utils import *


# Create abstract attacker
class AttackerBase(ABC):

    ip_addr = 'localhost'

    # Template method defn
    def templateMethod(self):
        # Attack pipeline
        self.discovery()
        self.main()
        self.reverseShell()


    # Defining the template attacker method steps
    
    # Methods with @abstractmethod annotation should be overriden in your custom attacker class.
    # Methods without @abstractmethod annotation are default methods 
        # which will be used by child classes if you don't override.


    def discovery(self) -> None:
        pass
        #print("Abstract attacker discovery called")


    def main(self) -> None:
        pass
        #print("Abstract attacker main called")

    @abstractmethod
    def reverseShell(self) -> None:
        pass
        #print("Abstract attacker reverseShell called")



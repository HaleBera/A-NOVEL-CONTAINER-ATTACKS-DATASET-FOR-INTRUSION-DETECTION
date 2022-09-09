Construct the Environment


  1. VM Configuraiton
  
      # Create a vagrant VM using "vagrant_creation_automater.sh".
      $ python3 vagrant_creation_automater.sh


      # Enter the name of the VM, which will be an attacker.
      $ CVE-2019-15107_Attacker1


      # Go to the path of the directory created by "vagrant_creation_automater.sh".
      $ cd vagrant_CVE-2019-15107_Attacker1


      # UP the new VM and establish an ssh connection with it.
      $ vagrant up && vagrant ssh  # Select eno1 (to select the first option, enter 1)
  

  2. Dependency Installation
      # Install dependencies using "vagrant_dependencies.sh"
      $ python3 vagrant_dependencies.sh


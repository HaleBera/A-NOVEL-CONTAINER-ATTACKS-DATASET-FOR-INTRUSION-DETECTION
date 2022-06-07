

Vagrant Installation

  1. ((!!!)Vagrant installation commands will be added soon ... )
  
  
  2. Install  "vagrant-scp plugin" to copy files between the host and the vagrant VMs.
     (https://howtoprogram.xyz/2017/08/13/copy-files-folders-host-guest-vagrant/)
     
     $ vagrant plugin install vagrant-scp 




VM Configuraiton

  # Create a vagrant VM.
  $ python3 vagrant_automate.sh


  # Enter the name of the VM, which will be an attacker.
  $ CVE-2019-15107_Attacker1


  # Go to the path of the directory created by "vagrant_automate.sh".
  $ cd vagrant_CVE-2019-15107_Attacker1


  # UP the new VM and establish an ssh connection with it.
  $ vagrant up & vagrant ssh  # Select eno1 (the first option)
  

OPTION 1: To use shared folders, overwrite "Vagrantfile" context in the vagrant_automate.sh, according to https://howtoprogram.xyz/2017/08/13/copy-files-folders-host-guest-vagrant/

OPTION 2: Clone the repo to yur host, and send the related attacker folder by using vagrant-scp plugin



Vagrant Installation

  1. ((!!!)Vagrant installation commands will be added soon ... )
  
  
  2. OPTION 1: You can use a shared folder to access attacker scripts.
          URL1: https://howtoprogram.xyz/2017/08/13/copy-files-folders-host-guest-vagrant/)
  
          - To use shared folders, overwrite "Vagrantfile" context in the vagrant_automate.sh, according to URL1


     OPTION 2: You can use vagrant-scp plugin to copy the access attacker scripts to the VM.
     
          - Clone the repo to yur host, and send the related attacker folder by using vagrant-scp plugin.
          
          - Install  "vagrant-scp plugin" the following command:     
            $ vagrant plugin install vagrant-scp 
           
           
     OPTION 3: You can use scp directly. (Permission Denied alınıyor)
     
              - Follow the URL1




Construct the Environment


  1. VM Configuraiton
  
      # Create a vagrant VM.
      $ python3 vagrant_automate.sh


      # Enter the name of the VM, which will be an attacker.
      $ CVE-2019-15107_Attacker1


      # Go to the path of the directory created by "vagrant_automate.sh".
      $ cd vagrant_CVE-2019-15107_Attacker1


      # UP the new VM and establish an ssh connection with it.
      $ vagrant up && vagrant ssh  # Select eno1 (the first option)
  
  
  2. Send attacker scripts to the VM (OPTION 2 is followed) (Yiğit)
      
      $ vagrant scp /home/hale/Desktop/CVE-2020-9483.pcap ubuntu-focal@127.0.0.1:/home/vagrant (Yiğit)

      Gives the error:
        hale@k8s-leader:~/vagrant_contset2$ vagrant scp vagrant scp /home/hale/Desktop/CVE-2020-9483.pcap ubuntu-               focal@127.0.0.1:/home/vagrant
        The machine with the name 'ubuntu-focal@127.0.0.1' was not found configured for this Vagrant environment.
        

       !!!! For OPTION 3, Permission Denied alınıyor (Yiğit)        



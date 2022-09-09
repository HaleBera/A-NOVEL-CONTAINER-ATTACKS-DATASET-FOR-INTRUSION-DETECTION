#!/bin/bash (URL0)

# A tutorial for Vagrant (URL1)

# Create a directory that your Vagrantfile will be standing on.
echo " *** Please enter the vagrant file name:"
read filename
vagrant_file_name="vagrant_$filename"
mkdir $vagrant_file_name


# Go to the created directory path
cd $vagrant_file_name


# Create a Vagrantfile (URL2)
touch Vagrantfile

# Write the following content into the Vagrantfile (URL3)

echo "Vagrant.configure(\"2\") do |config|" >> Vagrantfile
echo "  config.vm.box = \"ubuntu/focal64\"" >> Vagrantfile
echo "  config.vm.network \"public_network\"" >> Vagrantfile

echo "  config.vm.provider :virtualbox do |v|" >> Vagrantfile
echo "    v.customize [\"modifyvm\", :id, \"--uart1\", \"0x3F8\", \"4\"]" >> Vagrantfile
echo "    v.customize [\"modifyvm\", :id, \"--uartmode1\", \"file\", File::NULL]" >> Vagrantfile
echo "  end" >> Vagrantfile

echo "end" >> Vagrantfile

# Reference URL0: Bash Scripting http://www.compciv.org/topics/bash/scripting/
# Reference URL1: Vagrant Beginner Tutorial https://phoenixnap.com/kb/vagrant-beginner-tutorial#:~:text=Vagrant%20SSH,-You%20can%20connect&text=Once%20you%20are%20done%20exploring,the%20session%20with%20CTRL%2DD.
# Reference URL2: Creating a Vagrantfile https://mariadb.com/kb/en/creating-a-vagrantfile/
# Reference URL3: Bash Write-to-File https://linuxize.com/post/bash-write-to-file/#:~:text=In%20Linux%2C%20to%20write%20text,operators%20or%20the%20tee%20command.
# Reference URL4: Vagrant Freezes on 'SSH auth method: private key' https://github.com/hashicorp/vagrant/issues/11777
# Reference URL5: How to exit SSH of Vagrant in terminal https://superuser.com/questions/704032/how-to-exit-ssh-of-vagrant-in-terminal 


#vagrant up
#vagrant ssh

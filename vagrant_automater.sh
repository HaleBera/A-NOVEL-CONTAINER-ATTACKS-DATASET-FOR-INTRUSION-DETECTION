#Creating a Vagrantfile: https://mariadb.com/kb/en/creating-a-vagrantfile/
#Vagrant Beginner Tutorial: https://phoenixnap.com/kb/vagrant-beginner-tutorial#:~:text=Vagrant%20SSH,-You%20can%20connect&text=Once%20you%20are%20done%20exploring,the%20session%20with%20CTRL%2DD.
#How to exit SSH of Vagrant in terminal: https://superuser.com/questions/704032/how-to-exit-ssh-of-vagrant-in-terminal 

#SUBNET: 144.122.71.192/24
#Kubernetes Cluster IP: 144.122.71.18:8082


#!/bin/bash (http://www.compciv.org/topics/bash/scripting/)
# Create a directory that your Vagrantfile will be standing on.
echo " *** Please enter the vulnerability (CVE) in the YEAR-NUMBER  i.e. \"2019-15107\" format:"
read CVE_ID
vagrant_file_name="vagrant_$CVE_ID"
mkdir $vagrant_file_name
# rm -r vagrant_contsec (https://docs.oracle.com/cd/E19253-01/806-7612/files-20/index.html)
# Enter to the created directory
cd $vagrant_file_name
# Create a Vagrantfile (https://linuxhint.com/touch-command-linux/)
touch Vagrantfile
# Write the following content into the Vagrantfile (https://linuxize.com/post/bash-write-to-file/#:~:text=In%20Linux%2C%20to%20write%20text,operators%20or%20the%20tee%20command.)
#printf "Vagrant.configure("2") do |config|\n" $USER > Vagrantfile

echo "Vagrant.configure(\"2\") do |config|" >> Vagrantfile
#echo "  config.vm.box = \"ubuntu/focal64\"" >> Vagrantfile
echo "  config.vm.box = \"alpine/alpine64\"" >> Vagrantfile
echo "  config.vm.network \"public_network\"" >> Vagrantfile
echo "end" >> Vagrantfile
#  Up the vagrant and get an ssh connection (https://phoenixnap.com/kb/vagrant-beginner-tutorial#:~:text=Vagrant%20SSH,-You%20can%20connect&text=Once%20you%20are%20done%20exploring,the%20session%20with%20CTRL%2DD.)
#vagrant up
# select eno1 for bridge
# To keep execute bash commmands after getting the ssh add a "EOF" (https://stackoverflow.com/questions/26434604/bash-script-execute-commands-after-ssh)
#!/bin/bash (http://www.compciv.org/topics/bash/scripting/)
# Create a directory that your Vagrantfile will be standing on.
#echo " *** Please enter the vulnerability (CVE) in the YEAR-NUMBER  i.e. \"2019-15107\" format:"
#read CVE_ID
#vagrant_file_name="vagrant_$CVE_ID"
#mkdir $vagrant_file_name
# rm -r vagrant_contsec (https://docs.oracle.com/cd/E19253-01/806-7612/files-20/index.html)
# Enter to the created directory
#cd $vagrant_file_name
# Create a Vagrantfile (https://linuxhint.com/touch-command-linux/)
#touch Vagrantfile
# Write the following content into the Vagrantfile (https://linuxize.com/post/bash-write-to-file/#:~:text=In%20Linux%2C%20to%20write%20text,operators%20or%20the%20tee%20command.)
#printf "Vagrant.configure("2") do |config|\n" $USER > Vagrantfile
 
#echo "Vagrant.configure(\"2\") do |config|" >> Vagrantfile
#echo "  config.vm.box = \"ubuntu/focal64\"" >> Vagrantfile
#echo "  config.vm.network \"public_network\"" >> Vagrantfile
#echo "end" >> Vagrantfile
#  Up the vagrant and get an ssh connection (https://phoenixnap.com/kb/vagrant-beginner-tutorial#:~:text=Vagrant%20SSH,-You%20can%20connect&text=Once%20you%20are%20done%20exploring,the%20session%20with%20CTRL%2DD.)
#vagrant up
# select eno1 for bridge
# To keep execute bash commmands after getting the ssh add a "EOF" (https://stackoverflow.com/questions/26434604/bash-script-execute-commands-after-ssh)
#vagrant ssh << EOF
#echo "The current vagrant box's IP is:"
#ip a
#vagrant@ubuntu-focal:~$ ip a # learn vagrant box's ip address
#echo "befor EOF"
# Exit from the vagrant VM
#exit
#EOF
# Properly halt te vagrant
#vagrant halt
#echo "after EOF"

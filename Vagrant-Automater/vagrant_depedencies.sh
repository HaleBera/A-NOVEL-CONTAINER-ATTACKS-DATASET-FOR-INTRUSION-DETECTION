#!/bin/bash 

# https://askubuntu.com/questions/338857/automatically-enter-input-in-command-line

vagrant up
vagrant ssh

sudo apt update && sudo apt upgrade -y
sudo apt-get install nano
sudo apt-get install python3
sudo apt install net-tools     # To learn the VMs IP address, use "ifconfig" 
sudo apt-get install git -y

# Nuclei needed to be installed

#!/bin/bash (http://www.compciv.org/topics/bash/scripting/)

# nuclei kurmak icin;
#sudo apt update && sudo apt upgrade
#lsb_release -a
wget https://go.dev/dl/go1.18.linux-amd64.tar.gz
#ls /usr/local/go # distro's old go version, if exists; then $ 
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.18.linux-amd64.tar.gz


# add the following to `$HOME/.bashrc`
# https://askubuntu.com/questions/127056/where-is-bashrc

echo "export GOROOT=/usr/local/go" >> .bashrc
echo "export GOPATH=$HOME/go"   >> .bashrc
echo "export PATH=$GOPATH/bin:$GOROOT/bin:$HOME/.local/bin:$PATH"  >> .bashrc

 #https://stackoverflow.com/questions/54415733/getting-gopath-error-go-cannot-use-pathversion-syntax-in-gopath-mode-in-ubun
# should be updated according to the above url

# get a new shell/logout + login

exit 0

vagrant ssh

go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest


# clone the repointo each vagrant
git clone https://github.com/HaleBera/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION.git



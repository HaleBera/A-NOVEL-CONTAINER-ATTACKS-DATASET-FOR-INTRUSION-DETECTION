
sudo apt update
sudo apt-get install nano
sudo apt-get install python3
sudo apt install net-tools     # To learn the VMs IP address, use "ifconfig" 



# Nuclei needed to be installed

#!/bin/bash (http://www.compciv.org/topics/bash/scripting/)

# nuclei kurmak icin;
sudo apt update && sudo apt upgrade
lsb_release -a
wget https://go.dev/dl/go1.18.linux-amd64.tar.gz
ls /usr/local/go # distro's old go version, if exists; then $ 
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.18.linux-amd64.tar.gz


# add the following to `$HOME/.bashrc`
# https://askubuntu.com/questions/127056/where-is-bashrc

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$HOME/.local/bin:$PATH

# get a new shell/logout + login

exit

vagrant ssh

go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest







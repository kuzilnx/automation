#!/usr/bin/env bash 
#########################################
#created by: Shai
#purpose to install and setup ansible env
#date: 29/03/2021
#version: v1.0.1
########################################

get_ssh(){
hostname
ssh-keygen -b 2048 -t rsa -f /home/vagrant/.ssh/id_rsa2 -q -N ""
sleep 2
cat /home/vagrant/.ssh/id_rsa2.pub | tee -a /home/vagrant/.ssh/authorized_keys
hostname
sshd_conf="/etc/ssh/sshd_config"
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' $sshd_conf
sudo sed -i 's/GSSAPIAuthentication/#GSSAPIAuthentication/g' $sshd_conf
sudo sed -i 's/GSSAPICleanupCredentials/#GSSAPICleanupCredentials/g' $sshd_conf
sudo sed -i 's/PubkeyAuthentication no/PubkeyAuthentication yes/g' $sshd_conf
echo "sed done"
#sudo systemctl restart sshd
#ssh-copy-id -i /home/vagrant/.ssh/id_rsa2.pub vagrant@192.168.111.10
#ssh-copy-id -i /home/vagrant/.ssh/id_rsa2.pub vagrant@192.168.111.11
}

test_ansible(){
git clone -b Ansible https://gitlab.com/mondbev/flask.git
cd flask
pip3 install ansible
ansible-playbook deploy.yml
}
###
#Main
###
get_ssh
test_ansible

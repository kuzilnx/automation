#!/usr/bin/env bash 
#########################################
#created by: Silent-Mobius
#purpose to install and setup ansible env
#date: 08/03/2021
#version: v1.4.19
########################################
set -x
#Variables
_installer=${1:-'yum'}
_pkgs=(epel-release python3-pip)

#Functions
install_pkgs(){

	for _pkg in ${_pkgs[@]}
		do
			$_installer install -y $_pkg
		done

}

###
#Main
###
if [[ $EUID != 0 ]];then
	echo $msg_root
	exit 1
else

	install_pkgs
fi


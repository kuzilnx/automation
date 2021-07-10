#!/usr/bin/env bash

ip1="172.55.55."
ipool(){
local no_req=$1
echo "${ip1}${no_req}"
exit 0
}
[[ -z $1 ]] && exit 1 || ipool $1

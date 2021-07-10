#!/usr/bin/env bash
pip install requests_html
PODIP=$(microk8s kubectl describe pod | grep -e "^IP:" | awk '{print $2}')
sed -ri 's/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b'/"${PODIP}"/ test.py &> /dev/null
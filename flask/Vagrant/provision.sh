#!/usr/bin/env bash 
##################################################
#created by: loud-mobius(YAMS)
#purpose: autoprovision vagrant with tools for app deploy
#date: 01/03/2021
#version : v1.9.0
##################################################

_installer=yum
_pkgs=(epel-release git nginx python3-pip)
_project="/opt"
_gitrepo=https://gitlab.com/mondbev/flask.git


# install nginx --> flask --> gunicorn
install_tools(){

	for _pkg in ${_pkgs[@]}
		do
			$_installer install -y --nogpgcheck $_pkg
		done
}

get_app_from_git(){
	git clone $_gitrepo $_project  #path for app

	chown -R nginx:nginx $_project/app
}

init_app(){
	cd $_project/app
	pip3 install -r requirements.txt
}

conf_nginx(){
	mv /etc/nginx/nginx.conf{,.bak}
	echo -n '
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;
}
' > /etc/nginx/nginx.conf
	echo -n '
	server {
		listen 80;
		server_name 172.28.128.101;

		location / {
		proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
		proxy_pass http://unix:/opt/app/app.sock;
		}
	}' > /etc/nginx/conf.d/flask.conf
if [[ $(nginx -t > /dev/null; echo $?) == 0 ]];then
	systemctl enable --now nginx
else
	echo "there is an error with nginx conf"
fi
	
#sed -i.bak -n '38,57 s/^\s/#/gp' /etc/nginx/nginx.conf
}

systemd_conf(){
echo -n "	
[Unit]
Description=Flask Daemon
After=network.target

[Service]
User=nginx
Group=nginx
WorkingDirectory=/opt/app
ExecStart=/usr/local/bin/gunicorn  --workers 3 --bind unix:/opt/app/app.sock app:app

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/flask.service
 systemctl daemon-reload
 sleep 2
 systemctl enable --now flask
}

selinux_config(){
	sed -i 's/=enforcing/=permissive/g' /etc/selinux/config
	setenforce permissive
}

#####
#Main -_ - _ -_  -_  -_
####

if [[ $EUID != 0 ]];then
       echo "can NOT provision the server; Please use Root permission"
else
	selinux_config
 	install_tools
	conf_nginx
	get_app_from_git
	init_app
	systemd_conf
	echo "done"
fi


















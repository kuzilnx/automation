# Lab: NFS sharing storage for DNS and WEB servers
```sh 
  __ _| |_| |_ ___ _ __ | |_(_) ___  _ __ | |
 / _` | __| __/ _ \ '_ \| __| |/ _ \| '_ \| |
| (_| | |_| ||  __/ | | | |_| | (_) | | | |_|
 \__,_|\__|\__\___|_| |_|\__|_|\___/|_| |_(_)

 You need to run `export VAGRANT_EXPERIMENTAL="disks"` in order for this LAB to work
```
 


## Purpose of this LAB:

Well that's in the headline: 
To set up local environment of `virtualbox` or `vmware-workstation` with nfs share that provides storage to `httpd` (apache) webserver and to `bind` (named) dns server.

To deploy the lab you need `Vagrant` and `Ansible` installed on you host:

if debian based :

```sh
apt install -y vagrant ansible
```

if redhat based :

```sh
dnf install -y vagrant ansible
```
or if you have older version

```sh
yum install -y vagrant ansible
```
the playbooks that will run are stored as `roles` in roles folder and are managed as roles with `playbook.yaml` file.

## To start the LAB:

one can run `vagrant up` in project folder and should work automatically. 


> #### NOT for students: Please go over the code and study it.
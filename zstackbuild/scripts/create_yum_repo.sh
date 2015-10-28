#!/bin/bash
# You need to install a very clean and basic host to download the yum repo.
#rhel6
yum install -y unzip rabbitmq-server mysql-server mysql java-1.7.0-openjdk libselinux-python python-devel python-setuptools python-pip gcc autoconf iputils tcpdump ethtool haproxy dnsmasq wget curl qemu-img scsi-target-utils httpd openssh-clients openssh-server sshpass sudo ntp ntpdate bzip2 mysql qemu-kvm bridge-utils libvirt-python libvirt nfs-utils vconfig libvirt-client iptables tar gzip libaio lvm2 lvm2-utils device-mapper-multipath-libs device-mapper-multipath --downloadonly --downloaddir=repo 
#rhel7
#yum install -y unzip rabbitmq-server mysql-server mysql java-1.7.0-openjdk libselinux-python python-devel python-setuptools python-pip gcc autoconf iputils tcpdump ethtool haproxy dnsmasq wget curl qemu-img scsi-target-utils httpd openssh-clients openssh-server sshpass sudo ntp ntpdate bzip2 mysql qemu-kvm bridge-utils libvirt-python libvirt nfs-utils vconfig libvirt-client iptables tar gzip iptables-services mariadb mariadb-server libaio lvm2 lvm2-utils device-mapper-multipath-libs device-mapper-multipat --downloadonly --downloaddir=repo

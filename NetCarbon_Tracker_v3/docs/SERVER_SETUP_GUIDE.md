# Server Setup Guide — NetCarbon Tracker

Dokumentasi ini menjelaskan langkah-langkah konfigurasi tiap server
agar proyek *NetCarbon Tracker* dapat berjalan dengan baik.

## 1. Konfigurasi IP Address

## FW-SRV

source /etc/network/interefaces.d/*

auto lo
iface lo inet loopback

auto ens33
iface ens33 inet dhcp

auto ens34
iface ens34 inet static
	address 10.10.10.1
	netmask 255.255.255.248

auto ens35
iface ens35 inet static
	address 172.16.10.1
	netmask 255.255.255.248


## WEB-SRV

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

auto ens33
iface ens33 inet static
	address 10.10.10.2
	netmask 255.255.255.248
	gateway 10.10.10.1

## MAIL-SRV

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

auto ens33
iface ens33 inet static
	address 10.10.10.3
	netmask 255.255.255.248
	gateway 10.10.10.1

## INT-SRV

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

auto ens33
iface ens33 inet static
	address 172.16.10.5
	netmask 255.255.255.248
	gateway 172.16.10.1

# 2. Mengaktifkan IP Forwarding

## FW-SRV

sudo nano /etc/sysctl.conf
# Ubah baris berikut:
net.ipv4.ip_forward=1
sudo sysctl -p

# 3. Konfigurasi SSH & Key-based Authentication

## FW-SRV (Host utama monitoring)
apt install ssh
ssh-keygen -t rsa
ssh-copy-id monitor@10.10.10.2
ssh-copy-id monitor@10.10.10.3
ssh-copy-id monitor@172.16.10.5

## INT-SRV, WEB-SRV, MAIL-SRV

apt install ssh
nano /etc/ssh/sshd_config
#Ubah baris berikut:
PasswordAuthentication no
PermitRootLogin prohibit-password
PubkeyAuthentication yes

sudo systemctl restart ssh


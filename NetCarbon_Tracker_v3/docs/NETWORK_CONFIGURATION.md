# Network Configuration — NetCarbon Tracker Project

Dokumentasi ini berisi detail konfigurasi jaringan untuk setiap server
yang digunakan dalam proyek **NetCarbon Tracker**.

---

## Jaringan dan Subnet

1.  Zona : DMZ (Demilitarized Zone): 
    Subnet: 10.10.10.0
    Netmask: 255.255.255.248 (/29) 
    Deskripsi: Area publik (Web & Mail Server) 

2.  Zona: Internal (LAN) 
    Subnet: 172.16.10.0
    Netmask: 255.255.255.248 (/29)
    Deskripsi: Area privat (DNS/LDAP Server) |

---

## Server List & IP Address

Hostname, Interface, IP Address, Subnet, Role, dan Fungsi

1. Hostname: **FW-SRV**
   Interface: ens33
	IP Address: dhcp
	Subnet: Public
	Role: Gateway & Routing
   Interface: ens34 
	IP Address: 10.10.10.1
	Subnet: DMZ
	Role: Firewall & NetCarbon Tracker Host
   Interface: ens35
	IP Address: 172.16.10.1
	Subnet: Internal
	Role: Gateway ke jaringan internal & NetCarbon Tracker Host

2. Hostname: **WEB-SRV** 
   Interface: ens33
	IP Address: 10.10.10.2
	Subnet: DMZ
	Role: Web Server (LMS / HTTP Service)

3. Hostname: **MAIL-SRV** 
   Interface: ens33
	IP Address: 10.10.10.3
	Subnet: DMZ
	Role: Mail Server (Postfix / Roundcube)

4. Hostname: **INT-SRV**
   Interface: ens33
	IP Address: 72.16.10.5
	Subnet: Internal
	Role: Internal Server (DNS / LDAP Service)

---

## Routing & Forwarding

- **IP Forwarding:** Diaktifkan pada `FW-SRV`  
net.ipv4.ip_forward=1

- **Fungsi:** Menghubungkan komunikasi antara subnet `DMZ (10.10.10.0/29)` dan `INTERNAL (172.16.10.0/29)`

---

## SSH Access Scheme

| From | To | Protocol | Port | Keterangan |
|------|----|-----------|------|-------------|
| FW-SRV | WEB-SRV | SSH | 22 | Monitoring & Remote Access |
| FW-SRV | MAIL-SRV | SSH | 22 | Monitoring & Remote Access |
| FW-SRV | INT-SRV | SSH | 22 | Monitoring & Remote Access |

---

## Firewall (FW-SRV) — nftables Rules

| Chain | Policy | Rules |
|--------|----------|--------|
| **input** | drop | Accept loopback, SSH (tcp/22), ICMP |
| **forward** | drop | Allow SSH (tcp/22), ICMP |
| **output** | accept | Allow all outgoing traffic |

---

## Diagram Jaringan



```markdown
![Network Topology](TOPOLOGY_DIAGRAM.png)


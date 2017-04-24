Scanning:
=========

Nmap (Easy)
-----------

- What options would you use to get nmap to print the help summary?
  - `-h`
- What options would you use to set nmap to skip ping host discovery?
  - `-Pn`
- What options would you use to set nmap to the slowest scan setting?
  - `-T0`
- What options would you use to get nmap to use invalid checksums?
  - `--badsum`
- What options would you use to set nmap to fragment packets?
  - `-f`


Port Scanning (Medium)
----------------------

scanme.cityinthe.cloud

```
Starting Nmap 7.01 ( https://nmap.org ) at 2017-04-21 19:08 EDT
Nmap scan report for scanme.cityinthe.cloud (104.131.107.160)
Host is up (0.0076s latency).
Not shown: 65530 closed ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 eb:89:e7:f2:dc:c7:d8:8c:f1:d5:f9:f6:13:1a:fa:60 (RSA)
|_  256 72:e8:89:fd:f0:39:37:a9:a7:a4:65:a7:78:fd:67:fe (ECDSA)
25/tcp   open  smtp    Postfix smtpd
|_smtp-commands: ncl-spring-port.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
| ssl-cert: Subject: commonName=ncl-spring-port.localdomain
| Not valid before: 2017-04-21T03:56:43
|_Not valid after:  2027-04-19T03:56:43
|_ssl-date: TLS randomness does not represent time
53/tcp   open  domain  ISC BIND 9.10.3-P4-Ubuntu
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
1337/tcp open  http    nginx 1.10.3
|_http-server-header: nginx/1.10.3
|_http-title: Welcome to nginx!
Service Info: Host:  ncl-spring-port.localdomain; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.86 seconds
```

- What is the lowest-numbered open TCP port on this machine?
  - 21
- What is the second lowest-numbered open TCP port on this machine?
  - 22
- What is the third lowest-numbered open TCP port on this machine?
  - 25
- What is the fourth lowest-numbered open TCP port on this machine?
  - 53
- What is the version of the ssh server that is running on this machine?
  - OpenSSH 7.2p2
- What port is the HTTP server running on?
  - 1337
- What is the name of the software running the HTTP server?
  - nginx
- What is the version number of the HTTP server?
  - 1.10.3


Hidden Treasure (Hard)
----------------------

http://treasure.cityinthe.cloud/

robots.txt
```
User-agent: *
Disallow: /
Disallow: /mailocker
Disallow: /yipl
```

- What is the value of flag 1?
  - SKY-DIRN-5739
- What is the value of flag 2?
  - SKY-DIRN-4751
    - /yipl
- What is the value of flag 3?
  - SKY-DIRN-3981
    - /zztop1
- What is the value of flag 4?
  - SKY-DIRN-4618
    - /cocktail
    - DirBuster - lowercase big, fast
- What is the value of flag 5?
  - SKY-DIRN-5746
    - /mailocker
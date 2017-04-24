Log Analysis
============

DiG (Easy)
----------

- What is the IP address of the nameserver that was queried?
  - `208.67.220.220`
- How many A records are there for reddit.com?
  - `4`
- What service does Reddit use for their name servers?
  - `aws`
- What service does Reddit use to send emails for their application?
  - `mailgun`


VSFTPD (Easy)
-------------

- When was the first successful login? (round down to nearest minute)
  - `2017/03/20 17:46`
  - `grep "OK LOGIN" NCL-2017-Spring-vsftpd.log`
- How many successful logins were made?
  - `3`
  - `grep "OK LOGIN" NCL-2017-Spring-vsftpd.log | wc`
- How many successful uploads were made?
  - `25`
  - `grep "OK UPLOAD" NCL-2017-Spring-vsftpd.log | wc`
- How many total bytes were downloaded from the FTP server?
  - `6705766`
  - `grep "OK DOWNLOAD" NCL-2017-Spring-vsftpd.log | grep -Eo '[0-9]+( bytes)' | grep -Eo '[0-9]+' | awk '{s+=$1} END {print s}'`


Denial of Service (Easy)
------------------------

The Incident Response team has provided you with the contents of the /var/log directory after a denial of service attack. Help us locate the source of attack and any other damages.

- What is the tz name from the IANA time zone database of the timezone that the server is in?
  - `America/New_York`
  - [apt/term.log](var_log/apt/term.log)
- What is the MAC address of the server?
  - `52:54:00:aa:89:8f`
  - [upstart/network-interface-eth0.log](var_log/upstart/network-interface-eth0.log)
- When did the attack first start? (round to nearest minute)
  - `2015/11/28 15:58`
  - `grep 210.99.0.7 apache2/access.log -m5`
- How many requests were made as a part of the attack?
  - `???`
- At what time was there suspicious activity on the machine? (round to nearest minute)
  - `???`

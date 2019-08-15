# Library install hackinfo:
```bash
sudo python3 setup.py install 
pip3 install hackinfo
```


```python

from hackinfo import hackinfo 
hackinfo.nmap("www.google.com")

[+] <-- Running Nmap....[www.google.com] -->
Starting Nmap 7.70 ( https://nmap.org ) at 2019-08-15 17:12 UTC
Nmap scan report for www.google.com (172.217.3.100)
Host is up (0.0023s latency).
Other addresses for www.google.com (not scanned): 2607:f8b0:4006:801::2004
rDNS record for 172.217.3.100: lga34s18-in-f4.1e100.net

PORT     STATE    SERVICE
21/tcp   filtered ftp
22/tcp   filtered ssh
23/tcp   filtered telnet
80/tcp   open     http
110/tcp  filtered pop3
143/tcp  filtered imap
443/tcp  open     https
3389/tcp filtered ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 1.25 seconds
```
```python

hackinfo.reverseiplookup("www.facebook.com")
[+] <-- Running Reverseiplookup ....[www.facebook.com] -->
edge-star-mini-shv-01-sjc3.facebook.com
facebook.com
fbdogfoodbeta.com
mobileironbackup.com
purpletiesupport.com
star-mini.c10r.facebook.com
```


![Library_install_hackinfo](https://www.upload.ee/image/10356700/hejab_Library_install_hackinfo.png)


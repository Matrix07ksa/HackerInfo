#!/usr/bin/python
# -*- coding: utf-8 -*-
from termcolor import colored
import requests
import re 
import sys
import socket
import time
from bs4 import BeautifulSoup
from googlesearch import search
def write(M):
        for c in M + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(2. / 100)

class hackinfo():
        "web application Hejab Zaeri"
        global HackerScan
        HackerScan={
        "ping":"https://api.hackertarget.com/nping/?q=",
        "trcrouter":"https://api.hackertarget.com/mtr/?q=",
        "reversedns":"https://api.hackertarget.com/reversedns/?q=",
        "geoip":"https://api.hackertarget.com/geoip/?q=",
        "reverseiplookup":"https://api.hackertarget.com/reverseiplookup/?q=",
        "whois":"https://api.hackertarget.com/whois/?q=",
        "zonetransfer":"https://api.hackertarget.com/zonetransfer/?q=",
        "findshareddns":"https://api.hackertarget.com/findshareddns/?q=",
        "hostsearch":"https://api.hackertarget.com/hostsearch/?q=",
        "nmap":"https://api.hackertarget.com/nmap/?q=",
        "pagelinks":"https://api.hackertarget.com/pagelinks/?q=",
        "httpheaders":"https://api.hackertarget.com/httpheaders/?q=",
        "subnetcalc":"https://api.hackertarget.com/subnetcalc/?q=",
        "dnslookup":"https://api.hackertarget.com/dnslookup/?q="
        }
        def nmap (Target):
                Scan = HackerScan['nmap']
                write("[+] <-- Running Nmap....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))

        def ping(Target):
                Scan = HackerScan['ping']
                write("[+] <-- Running Ping....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def trcrouter(Target):
                Scan = HackerScan['trcrouter']
                write("[+] <-- Running Trcrouter ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def reversedns (Target):
                Scan = HackerScan['reversedns']
                write("[+] <-- Running Reversedns ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                                #re.match("\D+",Target).group().split(':')[1]
                        elif re.findall("error input is invalid",url):
                                ip = socket.gethostbyname(Target)
                                requests_url = Scan + ip
                                for url_ip in requests.get(requests_url).text.split("\n"):
                                        print(colored(url_ip,"green"))
                        else:
                                print(colored(url.strip(),"green"))
        def geoip(Target):
                Scan = HackerScan['geoip']
                write("[+] <-- Running Geoip ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def reverseiplookup (Target):
                Scan = HackerScan['reverseiplookup']
                write("[+] <-- Running Reverseiplookup ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def whois (Target):
                Scan = HackerScan['whois']
                write("[+] <-- Running Whois ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def zonetransfer (Target):
                Scan = HackerScan['zonetransfer']
                write("[+] <-- Running Zonetransfer ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def findshareddns(Target):
                Scan = HackerScan['findshareddns']
                write("[+] <-- Running Findshareddns ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def hostsearch(Target):
                Scan = HackerScan['hostsearch']
                write("[+] <-- Running HostSearch ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def pagelinks(Target):
                Scan = HackerScan['pagelinks']
                write("[+] <-- Running Pagelinks ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def httpheaders(Target):
                Scan = HackerScan['httpheaders']
                write("[+] <-- Running HttpHeaders ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def subnetcalc(Target):
                Scan = HackerScan['subnetcalc']
                write("[+] <-- Running Subnetcalc ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def dnslookup(Target):
                Scan = HackerScan['dnslookup']
                write("[+] <-- Running Dnslookup ....[{}] -->".format(Target))
                sys.stdout.flush()
                requests_url = Scan + Target
                requests_url = requests.get(requests_url)
                for url in requests_url.text.split("\n"):
                        if re.findall("error check your api query",url):
                                print(colored("[-] Error Chack ","red"))
                        else:
                                print(colored(url.strip(),"green"))
        def Dork_scan_sql(Target,cout):
                for i in search(Target,stop=int(cout)):
                        print(i) 
                        pa = "'" 
                        h = requests.get(i+pa) 
                        soup = BeautifulSoup(h.content,'html.parser') 
                        if len(soup.find_all(text=re.compile("SQL syntax"))) >0:
                                
                             print(colored("[SQL Found]=="+i,"green")) 
                             open("SQL-injection","a").write("[SQL Found]=="+i+"\n")
                        elif len(soup.find_all(text=re.compile("Warning"))) >0:
                             print(colored("[SQL Found]=="+i,"green")) 
                             open("SQL-injection.txt","a").write("[SQL Found]=="+i+"\n")
                        else:
                                print(colored("[No SQL Found ]","red"))                 
                
                






	

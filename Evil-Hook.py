import re
from bs4 import BeautifulSoup as bs
import requests
import sys
import argparse
from colorama import Fore


print(Fore.YELLOW+"""
 _______________________________________________
|############## EVIL - HOOK ###################|      
|        |                                     |
|        |              __,                    |
|        |           .-'_-'`                   |
|        |         .' {`                       |
|        |     .-'````'-.    .-'``'.           |
|        |   .'(0)       '._/ _.-.  `\         |
|        ¿  }     '. ))    _<`    )`  |        |
|            `-.,\'.\_,.-\` \`---; .' /         |
|               )  )       '-.  '--:           |
|                ( ' (          ) '.  \        |
|                 '.  )      .'(   /   )       |
|                   )/      (   '.    /        |
|                            '._( ) .'         |
|                                ( (           |
|                                 `-.          |
|                                              |
|______________________________________________|
|          Last Updated:13/05/2020             |
|   Author:SAGAR;@ http://github.com/S4GAR/    |
|______________________________________________|                                                                                                                                              
""")                                                  

parser = argparse.ArgumentParser()
parser.add_argument("-u",action="store",metavar="URL",help="eg:https://example.com/")
args = parser.parse_args()

class evil:
    def __init__(self,url):
        self.url = url
        evil.bringout(self)
    def pagedata(self):
        r = requests.get(self.url)
        soup = bs(r.text,'lxml')
        return str(soup)
    def bringout(self):
        heart = re.findall(r"[A-Za-z.\-]*\w+\@[A-Za-z_0-9\-]*\.\w+[.a-z]*",evil.pagedata(self))
        heart = set(heart)
        cnt = 0
        if len(heart) > 0:
            print(Fore.BLUE+"[+]Emails Found.")
            for blood in heart:
                print(Fore.CYAN,cnt+1,blood)
                cnt +=1
        else:
            print(Fore.RED+"[-]nothing found:{")

if args.u:
    url = args.u
    print(Fore.MAGENTA+"[+] URL :"+url)
else:
    print(Fore.RED+"[*]Error occured!! use -u to insert email.")

data = evil(url)


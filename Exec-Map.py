#!/usr/bin/python3
#Exec - Map
from os import *
from colorama import *
init(autoreset=True)
banner="""
 /$$$$$$$$                                     /$$      /$$                    
| $$_____/                                    | $$$    /$$$                    
| $$       /$$   /$$  /$$$$$$   /$$$$$$$      | $$$$  /$$$$  /$$$$$$   /$$$$$$ 
| $$$$$   |  $$ /$$/ /$$__  $$ /$$_____/      | $$ $$/$$ $$ |____  $$ /$$__  $$
| $$__/    \  $$$$/ | $$$$$$$$| $$            | $$  $$$| $$  /$$$$$$$| $$  \ $$
| $$        >$$  $$ | $$_____/| $$            | $$\  $ | $$ /$$__  $$| $$  | $$
| $$$$$$$$ /$$/\  $$|  $$$$$$$|  $$$$$$$      | $$ \/  | $$|  $$$$$$$| $$$$$$$/
|________/|__/  \__/ \_______/ \_______/      |__/     |__/ \_______/| $$____/ 
                                                                     | $$      
                                                                     | $$      
                                                                     |__/ 
    Coding By Mah-Coder | https://github.com/C0derByM4H6301/ 
    Dozens of features are being coded to be added, now demo and less features
    Dozens of features are being coded to be added, now demo and less features
    Dozens of features are being coded to be added, now demo and less features"""
print(Fore.GREEN+banner)
if getuid() != 0:
    print("Please run as root user")
    print("Examples:")
    print("root@kali:~# python3 a.py")
    print("kali@kal:~$ sudo python3 a.py")
panel="""
[1]: Nmap Scan
[2]:
[3]:
U: Update
E: Exit 
"""
print(Fore.RED+panel)

sh=input(Fore.BLACK+Back.CYAN+"=:>>"+Fore.RESET+Back.RESET+" ")
if sh=="1":
    sh1=input("Target: ")
    sh1_1="""
    1: Standard Scan
    2: TCP SYN port scan
    3: TCP connect port scan
    4: UDP port scan
    """

    print(sh1_1)
    sh1_2=input(":>>")

    if sh1_2=="1":
        system(f"nmap {sh1} ")
    if sh1_2=="2":
        system(f"nmap -sS {sh1}")
    if sh1_2=="3":
        system(f"nmap -sT {sh1}")
    if sh1_2=="4":
        system(f"nmap -sU {sh1}")

else:
    print("please use 1,2,3,U,u,E,e")
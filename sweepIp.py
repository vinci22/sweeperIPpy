from ast import For
import datetime
import os
import getmyIp
from art import *
from termcolor import colored, cprint

tprint("SWEEPER IP",font="cybermedium",)

ip_parts = str(getmyIp.myIp).split(".")
ip_format=ip_parts[0]+"."+ip_parts[1]+"."+ip_parts[2]+"."+ip_parts[3]
net_ip = ip_parts[0]+"."+ip_parts[1]+"."+ip_parts[2]+"."
frist_host = 1
last_host = 254
last_host += 1
time1 = datetime.datetime.now()
cprint(f"Scaneando red.....Ip--->{net_ip}\n","green")

for ip in range(frist_host,last_host):
    i=0
    adrr = net_ip + str(ip)
    command = "ping -c 1 " + adrr
    respon = os.popen(command)
    List = respon.readlines()
    if ("1 received" in List[4]):
        cprint(adrr+"---> Live","blue")

    else:
        cprint(f"{adrr}---> Death","yellow")
        #print(f"\033[5m\033[90;5;91m{adrr}--> Death\033[00m")

time2=datetime.datetime.now()

cprint(f"Net Scanned ----{time2-time1}","green",attrs=['blink'])
print("\a")
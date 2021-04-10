from netmiko import ConnectHandler
import datetime
import getpass
import os

user = 'username'
pw = 'password'
date = datetime.date.today()
ip_addr = ("192.168.108.129")

netDevice = {
    'ip': ip_addr,
    'device_type': 'cisco_ios',
    'username': user,
    'password': pw,
    'port': 22,
    }


def ciscoRunConf():
    user = input('Please enter your username: ')
    pw = getpass.getpass(prompt='Please enter your password: ')
    net_connect = ConnectHandler(**netDevice)
    output = net_connect.send_command("show run")
    print(output, file=open("%s.txt" % date, "a+"))

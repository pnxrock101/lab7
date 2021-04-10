import os
import netmiko
import datetime

user = 'username'
pw = 'password'
date = datetime.date.today()
netDevice = {
    'ip': 'ip_address',
    'device_type': 'cisco_ios',
    'username': user,
    'password': pw
    }


def ciscoRunConf:
    user = input('Please enter your username: ')
    pw = getpass('Please enter your password: ')
    net_connect = ConnectHandler(**netDevice)
    output = net_connect.send_command("show run")
    print(output, file=open("%s.txt" % date, "a+")
    

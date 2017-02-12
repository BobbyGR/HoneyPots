import subprocess
import hipchat
import re
import socket

hipster = hipchat.HipChat(token='TEMP')
room_id = TEMP
from_name = 'ATLHoney'
message_color = "red"
log_location = '/var/log/nginx/access.log'
flushfile = False
captured = False
hostname = socket.gethostname()

def restart_service(name):
    command = ['/usr/sbin/service', name, 'restart']
    subprocess.call(command, shell=False)

with open(log_location, "r") as nginx_logs:
     for line in nginx_logs:
        if captured == False: 
         re1='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'    # IPv4 IP Address 1
         rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
         m = rg.search(line)
         if m:
            ipaddress1=m.group(1)
            try:
                     ipaddress1 = str(socket.gethostbyaddr(ipaddress1))
                     message = ipaddress1 + " has just accessed " + hostname + ".  Please review this machine. notice:nginx,80"
            except:
                     message = ipaddress1 + " has just accessed " + hostname + ".  Please review this machine. notice:nginx,80,dns_fail"
            hipster.message_room(room_id, from_name, message, color=message_color)
            flushfile = True
            captured = True
if flushfile == True:
   open(log_location, 'w').close()
   restart_service('nginx')


import subprocess
import hipchat
import re
import socket

hipster = hipchat.HipChat(token='TEMP')
room_id = TEMP
from_name = 'ATLHoney'
message_color = "red"
log_location = '/var/log/mariadb/mariadb.log'
flushfile = False
captured = False
hostname = socket.gethostname()

def restart_service(name):
    command = ['/usr/sbin/service', name, 'restart']
    subprocess.call(command, shell=False)

with open(log_location, "r") as mariadb_logs:
     for line in mariadb_logs:
        if captured == False:
         if re.match('(.*)Warning(.*)',line):
          re1='.*?'
          re2='(\\\'.*?\\\')'
          rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
          m = rg.search(line)
          if m:
             ipaddress1=m.group(1)
             try:
                     ipaddress1 = str(ipaddress1)
                     ipaddress1 = ipaddress1.replace("'","")
                     ipaddress1 = str(socket.gethostbyaddr(ipaddress1))
                     message = ipaddress1 + " has just accessed " + hostname + ".  Please review this machine. notice:mysql;3306"
             except:
                     message = ipaddress1 + " has just accessed " + hostname + ".  Please review this machine. notice:mysql;3306;dns_failed"
             hipster.message_room(room_id, from_name, message, color=message_color)
             #print message
             flushfile = True
             captured = True
if flushfile == True:
   open(log_location, 'w').close()
   restart_service('mariadb')

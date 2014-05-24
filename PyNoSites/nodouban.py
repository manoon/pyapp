# -*- coding:utf-8 -*-
import os
import time
import sys
from shutil import copy
def hostbak ():
	hostbak_path= '/etc/hosts.bak'
	host_path='/etc/hosts'
	cron_path="./nodouban.cron"
	copy(host_path,hostbak_path)
	print "Hosts File Backup Okay!"
	copy("./nodouban.py","/var/root/nodouban.py")
	copy(cron_path,"/var/root/nodouban.cron")
	time.sleep(5)
	os.system("crontab -u root /var/root/nodouban.cron")
	print "Cron File Installed Okay!"
def hostlock(hostlists):
	host_path='/etc/hosts'
	host_file=open(host_path,'a+')	
	


	try:
	    host_file.writelines("\n")	
	    for h in hostlists:
		host_file.writelines(h)
		#print h
	    print "恭喜你！祝你天天开森!"
	    print "no zuo no die,no douban no waste time"
	    print "解锁模式请运行 sudo python nodouban unlock"


	finally:

	    host_file.close()

def hostunlock(hostlists):
	host_path='/etc/hosts'
	host_file=open(host_path,'r')	
	
	def unlock(file,site):
		lines=file.readlines()
		newlines=[]
	        for line in lines:
			if site in line:
				line=""
				print "catch!"
			else:
				print "no"	
			newlines.append(line)
				
		return newlines		
		file.close()
	try:
	    for h in hostlists:
		newlines=unlock(host_file,h)
		
		host_file_w=open(host_path,'w')	


		for line in newlines:
			#print line
			host_file_w.write(line)
				

	    print "恭喜你！祝你天天开森!"

	finally:

	    host_file.close()

if __name__ == "__main__":
    hostlists = ["127.0.0.1 www.douban.com"]
    action=sys.argv[1]
    if os.path.exists("/var/root/nodouban.py"):
	print "Well Done,It works"
    else:
	print "Start Work"
    	hostbak()
    stop=0
    """
    hostlists=[]
    while not stop:
	host=raw_input("输入你想戒掉的网站，或者输入ok以保存 :\n")
	hostlist="127.0.0.1  "+host+" \n"
	if host=="ok":
		stop=1
	hostlists.append(hostlist)
    """
    if action=="unlock":
	curtime=time.strftime("%H:%M:%S").split(':')[0]
	print curtime
	if (int)(curtime)==22:
    		hostunlock(hostlists) 
	elif (int)(curtime)==11:
    		hostunlock(hostlists) 
	else:
		print "Sorry ^_^,There is no time to play!!!!Except 22:00-23:00"
    elif action=="lock":
    	hostlock(hostlists) 
    else:
	print "no action"
	exit(0)

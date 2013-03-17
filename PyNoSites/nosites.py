# -*- coding:utf-8 -*-
import os
import sys
from shutil import copy
def hostbak ():
	hostbak_path= 'C:\\WINDOWS\\system32\\drivers\\etc\\hosts.bak'
	host_path='C:\\WINDOWS\\system32\\drivers\\etc\\hosts'
	copy(host_path,hostbak_path)
	print "Hosts File BackupED!"
def getRights ():
	os.system('cacls c:\windows\system32\drivers\etc\hosts /grant Everyone:F')
	print "Get the Rights"
def hostattach(hostlists):
	host_path='C:\\WINDOWS\\system32\\drivers\\etc\\hosts'
	host_file=open(host_path,'a+')	


	try:
	    host_file.writelines("\n")	
	    for h in hostlists:
		host_file.writelines(h)
	    print "恭喜你！祝你天天开森!"

	finally:

	    host_file.close()

if __name__ == "__main__":
    #hostlist = ["127.0.0.1 letsgo.com"]
    stop=0
    hostlists=[]
    while not stop:
	host=raw_input("输入你想戒掉的网站，或者输入ok以保存 :\n")
	hostlist="127.0.0.1  "+host+" \n"
	if host=="ok":
		stop=1
	hostlists.append(hostlist)
    #print hostlists[:-1]
    #hosts=[]
    
    """
    for h in hostlists:
	
	h="127.0.0.1  "+h+" \n"
	print h
	hosts.append(h)
    print hosts
    """
    getRights()
    hostbak()
    hostattach(hostlists[:-1]) 
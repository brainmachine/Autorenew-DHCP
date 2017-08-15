import urllib2
import os
import time
import getpass

pwd = getpass.getpass()

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        print("Google responded, everything is fine.")
        return True
    except urllib2.URLError as err: 
        return False

while(True):
	if not internet_on():
		print("renewing DHCP")
		command = 'sudo networksetup -setdhcp Wi-Fi'
		p = os.system('echo %s|sudo -S %s' % (pwd, command))
	time.sleep(10)
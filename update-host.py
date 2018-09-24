#!/usr/bin/env python
import urllib2
import requests
import time

username = "your username"
password = "your password"
hostname = "your hostname"

APIbase = "https://"+username+":"+password+"@www.dnsdynamic.org/api/?hostname="+hostname+"&myip="
SLEEP_TIME = 100
hostname = ""
newHostname = ""

def main():
    print("Update DNS started")
    first = True
    while True:
        if first:
            first = False
            hostname = GetHostname()
            print ("initial run")
            Update(hostname)
        else:
            newHostname = GetHostname()
            if (newHostname == hostname):
                print("No update")
            else:
                print("IP changed, updating")
                Update(newHostname)
                hostname = newHostname
        time.sleep(SLEEP_TIME)

def Update (hostname):
    print("updating to: " + hostname)
    API = APIbase+hostname
    try:
        r = requests.get(API)
        print(r.status_code)
        print(r.text)
        #print(r.json)
    except:
        return

def GetHostname ():
    try:
        return urllib2.urlopen('http://ip.42.pl/raw').read()
    except:
        return "failed"

main()

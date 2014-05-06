# https://docs.python.org/dev/library/subprocess.html
# http://stackoverflow.com/questions/4785244/how-would-i-search-a-text-file-in-python


import  subprocess
import time

#GET IP FOR PI

def getIP():
    # first output results of nmap into file called nmap_results.txt
    subprocess.call(["nmap","-p80","-PN","--open","-sV", "-oG", "nmap_results.txt", "192.168.1.0/24"])

    #open nmap_results.txt, search for vera IP, and print it if it's found
    #(nmap_results.txt should be in same dir as this script)
    with open("nmap_results.txt", "r") as searchfile:
        for line in searchfile:
            if "lighttpd" in line: 
                print line
                vera = line.split()
                print vera[1]
                return vera[1]
    return ''


#ToggleLamp
def toggleLamp(IP, newstate):
    state = 0
    if newstate == 'lite on':
        state = 1
    
    url = "'http://%s:3480/data_request?id=lu_action&DeviceNum=5&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=%d'" % (IP,state)
    print url
    subprocess.call("wget "+url, shell=True)
'''
ip = getIP()
toggleLamp(ip, 'lite on');
time.sleep(3)
toggleLamp(ip, 'lite off');
time.sleep(3)
toggleLamp(ip, 'lite on');
time.sleep(3)
toggleLamp(ip, 'lite off');
'''

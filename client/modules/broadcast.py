#Found this code at: http://svn.python.org/projects/python/branches/pep-0384/Demo/sockets/broadcast.py

# Send UDP broadcast packets

MYPORT = 1028

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#CHANGE THIS-- once we get the hub listening, shouldn't need to loop. 
while 1:
    data = 'hello'
    s.sendto(data, ('<broadcast>', MYPORT))
    time.sleep(2)


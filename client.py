import sys
import socket
import time

if(len(sys.argv) != 3):                
    print "usage: a.out port filename"
    exit(1);

portA = sys.argv[1] #5678
inputA = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', int(portA)))

def connection(portA, values):
    s.send(str(values))
    s.close

try:
    f = open(inputA);
    for line in f:
	line = line.strip('\n')
	line = line.replace('$', '')
	words = line.split(' ')
	for w in words:
	    print w
	    connection(portA, w);
	    time.sleep(.1)
    connection(portA, "end");
    f.close()	

except Exception as ex:
   print ex
   exit(1);
    

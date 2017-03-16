import sys
import socket
import time
portA = 5678

def commands():
    if(len(sys.argv) != 3):
        print "usage: a.out port filename"
        exit(1);
#    print sys.argv[0]
#    print sys.argv[1]
#    print sys.argv[2]

#def connection(portA, values):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', int(portA)))

def connection(portA, values):
    print "Client: connected"    
    s.send(str(values))
    s.close


#commands()
try:
    values = ""
    f = open(sys.argv[1]);
    for line in f:
	line = line.strip('\n')
	words = line.split(' ')
	for w in words:
	    print w
#	    values += w + " "
	    connection(portA, w);
	    time.sleep(.1)
	
    connection(portA, "end");

except Exception as ex:
   print ex
   exit(1);
    
print(values)  
#portA = sys.argv[1]
portA = 5678
#connection(portA, values)                   

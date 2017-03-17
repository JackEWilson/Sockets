import sys
import socket
import time

if(len(sys.argv) != 3):                
    print "usage: python client.py port filename"
    exit(1);

portA = sys.argv[1] #global port given in cmd line arg
inputA = sys.argv[2] #globat input file of transactions

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', int(portA)))

def connection(portA, values):
    s.send(str(values))
    s.close

try: #parses through txt file and sends information line by line
    f = open(inputA);
    for line in f:
	line = line.strip('\n')
	line = line.replace('$', '')
#	print 'C: ', line
	connection(portA, line) #sends line
        time.sleep(.15) #had issues of it sending everything to same recv in server.
    connection(portA, "end end end"); #when done sends a buncha 'end'
    f.close()	

except Exception as ex:
   print ex
   exit(1);
    

import socket
import sys
import threading
import time

mutex = threading.Lock()
Database = {'jack': 2000, 'aohnny': 1999 }


def fx(arg):
    mutex.acquire()
    print arg, ": is running..."
    if(arg == 5):
	time.sleep(14)

    mutex.release()

threads = []

#for i in range(10):
#    t = threading.Thread(target=fx, args=(i,))
#    t.start()
#    threads.append(t)

#for t in threads:
#    t.join()


print Database

def printToLog():
    f = open("log.txt", "a")
    for key, value in sorted(Database.items()):
	f.write('%s %s\n' % (key, value))
    f.close()

try:
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 5678))
	s.listen(5)
	print "Server: waiting to accept()"
	(conn, addr) = s.accept()
	print 'Server: accepted with address', addr
	check = 1
    	while check == 1 :
		data1 = conn.recv(80)
		if(data1 != "end"):
			print "Server: received", data1
			data2 = conn.recv(80)
			print "Server: received", data2
			data3 = conn.recv(80)
			print "Server: received", data3
			print "Server: conn?", conn
			x = 0
			if(data2 == "credit"):
				if data1 in Database.keys():
					x = Database[data1]   
					x += int(data3)
					Database[data1] = x
				else:
			    		Database[data1] = data3
			if(data2 == "debit"):
				if data1 in Database.keys():
					x = Database[data1]      
	    	    			x -= int(data3)
	        			Database[data1] = x
	        		else:
					Database[data1] = (int(data3)*-1)    
		else:
	    		check = 0
	printToLog();
	s.close()
	
except Exception as err:
    print err
    exit(1)


print Database

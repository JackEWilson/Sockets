import socket
import sys
import threading
import time
import signal

mutex = threading.Lock() #mutex
Database = {} #dict
threads = [] #keep track of threads

if(len(sys.argv) != 2):                
    print "usage: python server.py port"
    exit(1)
else:
    portA = sys.argv[1] #Global port given as cmd line arg

def catchSignal(x, f): #catches kill signal, joins threads, prints to log.txt, and closes socket
	for t in threads:
		t.join()
	printToLog()
	s.close()

def printToLog(): #prints sorted dict to log.txt
	f = open("log.txt", "w")
	for key, value in sorted(Database.items()):
		f.write('%s $%s\n' % (key, value))
	f.close()

def handleThreads(conn):
	check = 1
	while check == 1:
		line = conn.recv(80) #receives information from client line by line
		words = line.split(' ')
		data1 = words[0]
		data2 = words[1]
		data3 = words[2]
		try:
			float(data3) #makes sure data3 is float
		except ValueError:
			print "found float"
			data2 = "end"
		if(data1 != "end" and data1 != ""):
			x = 0
			mutex.acquire() #starts mutex when accessing global dict
			if(data2 == "credit"):
				if data1 in Database.keys():
					x = float(Database[data1])   
					x += float(data3)
					Database[data1] = float(x)
				else:
					Database[data1] = float(data3)
			elif(data2 == "debit"):
				if data1 in Database.keys():
					x = float(Database[data1])  
					x -= float(data3)
					Database[data1] = x
				else:
					Database[data1] = (float(data3)*-1)
			mutex.release()
		else:
			check = 0 #ends thread
			conn.close()

try:
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM) #global socket
	s.bind(('localhost', int(portA)))
	s.listen(5)
	while True:
		signal.signal(signal.SIGINT, catchSignal)
		(conn, addr) = s.accept() 
		t = threading.Thread(target=handleThreads, args=(conn,))
		t.start()
		threads.append(t) #keeps track of threads

except Exception as err:
	print err
	exit(1)

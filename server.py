import socket
import sys
import threading
import time
import signal

mutex = threading.Lock()
Database = {}
threads = []

if(len(sys.argv) != 2):                
    print "usage: a.out port"
    exit(1)
else:
    portA = sys.argv[1]

def catchSignal(x, f):
	for t in threads:
		t.join()
	printToLog()
	s.close()

def printToLog():
	f = open("log.txt", "w")
	for key, value in sorted(Database.items()):
		f.write('%s $%s\n' % (key, value))
	f.close()

def handleThreads(conn):
	check = 1
	while check == 1:
		data1 = conn.recv(80)
		if(data1 != "end" and data1 != ""):
			data2 = conn.recv(80)
			data3 = conn.recv(80)
			x = 0
			mutex.acquire()
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
			check = 0
			conn.close()

try:
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', int(portA)))
	s.listen(5)
	while True:
		signal.signal(signal.SIGINT, catchSignal)
		(conn, addr) = s.accept()
		t = threading.Thread(target=handleThreads, args=(conn,))
		t.start()
		threads.append(t)

except Exception as err:
	print err
	exit(1)

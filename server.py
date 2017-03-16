import socket
import sys
import threading
import time
import signal

mutex = threading.Lock()
Database = {}
threads = []

#for i in range(10):
#t = threading.Thread(target=fx, args=(i,))
#t.start()
#threads.append(t)

#for t in threads:
#t.join()

#def fx(arg):
#	mutex.acquire()
#	print arg, ": is running..."
#	if(arg == 5):
#	time.sleep(14)
#
#	mutex.release()

def catchSignal(x, f):
	for t in threads:
		t.join()
	print Database
	printToLog()
	print "made it babe"
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
			print "Server: received d1", data1
			data2 = conn.recv(80)
			print "Server: received d2", data2
			data3 = conn.recv(80)
			print "Server: received d3", data3
			print "Server: conn? ", conn
			x = 0
			if(data2 == "credit"):
				if data1 in Database.keys():
					x = int(Database[data1])   
					x += int(data3)
					Database[data1] = int(x)
				else:
					Database[data1] = int(data3)
			if(data2 == "debit"):
				if data1 in Database.keys():
					x = int(Database[data1])  
					x -= int(data3)
					Database[data1] = x
				else:
					Database[data1] = (int(data3)*-1)
		else:
			check = 0
			conn.close()


try:
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 5678))
	s.listen(5)
	print "Server: waiting to accept()"
	while True:
		signal.signal(signal.SIGINT, catchSignal)
		(conn, addr) = s.accept()
		print 'Server: accepted with address', addr
		t = threading.Thread(target=handleThreads, args=(conn,))
		t.start()
		threads.append(t)


except Exception as err:
	print err
	exit(1)

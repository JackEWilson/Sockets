import socket
import sys
import threading
import time
import signal

mutex = threading.Lock()
Database = {}
threads = []

def catchSignal(x, f):
	printToLog();
	print "made it babe"
	s.close()

def fx(arg):
	mutex.acquire()
	print arg, ": is running..."
	if(arg == 5):
		time.sleep(14)

	mutex.release()



def printToLog():
	f = open("log.txt", "w")
	for key, value in sorted(Database.items()):
		f.write('%s %s\n' % (key, value))
	f.close()


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
def begin():
	try:
		s.bind(('localhost', 5678))
		s.listen(5)
		print "Server: waiting to accept()"
		check1 = 1
		signal.signal(signal.SIGINT, catchSignal)
		(conn, addr) = s.accept()
		print 'Server: accepted with address', addr
		check = 1
		i = 0;
		obj = []	
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
				i += 1
				obj = [data1, data2, data3]
	#			t = threading.Thread(target=dataHandler, args=(i,obj))
	#			t.start()
	#			threads.append(t)
			else:
				check = 0;
		time.sleep(5)
		for t in threads:
			t.join()


	except Exception as err: 
		print err
		exit(1)
		printtoLog()

def dataHandler(i, obj):
		mutex.acquire()
		data1 = obj[0]
		data2 = obj[1]
		data3 = obj[2]
		print i, " thread is here"
		if(data2 == "credit"):
			if data1 in Database.keys():
				x = int(Database[data1])   
				x += int(data3)
				Database[data1] = x
			else:
				Database[data1] = int(data3)
		if(data2 == "debit"):
			if data1 in Database.keys():
				x = int(Database[data1])  
				x -= int(data3)
				Database[data1] = x
			else:
				Database[data1] = (int(data3)*-1)
		mutex.release()
	
begin()
print Database

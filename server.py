import socket
import sys


try:
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 5678))
	s.listen(5)

	print "Server: waiting to accept()"
#	(conn, addr) = s.accept()

	print 'Server: accepted with address', addr

#	data = conn.recv(80)
	print "Server: received", data


	s.close()


except Exception as err:
	print err
	exit(1)

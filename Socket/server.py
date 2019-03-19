import socket
from address import Address
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '192.168.171.227'
port = 8083

server.bind((address, port))
server.listen(5)

print("Server running")
print("Listening on {add}:{port}".format(add = address, port = port))


while True:
	conn, addr = server.accept()
	print("New connection acquired: {conn}, {addr}".format(conn = conn, addr = addr))

	filename = 'From Server/Image.jpg' 
	f = open(filename, 'rb')
	length = 0
	for data in f:
		conn.sendall(data)
		length += len(data)/(1024*1024)
		print("MBs send: {length}".format(length = length))
	print("Put Successfull")

	print("Done!")
	conn.shutdown(socket.SHUT_WR)
	print("Client disconnected")

	print("Exit (y/Y): ")
	choice = sys.stdin.read(1)
	if choice != 'y' and choice != 'Y':
		break

	
server.close()
print("Server closed!!")

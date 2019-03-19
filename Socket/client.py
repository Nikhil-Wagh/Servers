import socket
import time
import os

address = '192.168.171.227'
port = 8083

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address, port))

filename = 'To Client/Image.jpg'
f = open(filename, 'wb')
start = time.clock()
length = 0
while True:
	data = client.recv(1024 * 1024 * 1024)
	length += len(data)/(1024*1024)
	print("MBs received: {length}".format(length = length))
	if not data:
		break
	f.write(data)

f.close()
total_time = time.clock() - start
client.close()

statinfo = os.stat(filename)
total_bytes = statinfo.st_size
print("Done Receiving")
print("Average Speed: {bytes} bytes in {time} sec \n{speed} MB/sec".format(bytes = total_bytes, time = total_time, speed = total_bytes/(1024*1024*total_time)))
import socket
host = "127.0.0.1"
port = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))
f= open('Myfile2.txt','wb')
print('New file created')
data, addr = sock.recvfrom(1024)
while(data):
 print(data)
 if data.decode("utf-8")=="Now":
 break
 f.write(data)
 data, addr = sock.recvfrom(1024)
print('File is successfully received!!!')
f.close()
f = open('Myfile2.txt','r')
print(f.read)
f.close()
sock.close()
print('Connection closed!')
@client.py
import socket
host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'Myfile.txt'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
f = open("Myfile.txt", "r")
data = f.read(buffer_size)
while data:
 print(data)
 if(sock.sendto(str.encode(data), (host, port))):
 data = f.read(buffer_size)
sock.sendto(str.encode("Now"),(host, port))
sock.close()
f.close()
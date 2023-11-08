import socket
from time import sleep
IP="127.0.0.1"
port=53533
packet1="TYPE=A\nNAME=fibonacci.com\nVALUE=0.0.0.0\nTTL=1"
packet2="TYPE=A\nNAME=fibonacci.com"
socktwo=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(packet1.encode(),(IP,port))

sleep(1)
socktwo.bind(("127.0.0.1",2020))
socktwo.sendto(packet2.encode(),(IP,port))
print(socktwo.recv(1024))
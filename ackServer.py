import socket, sys
import random

#Karnvir Basra
#Arshpreet Dhillon 104932740
# Create a TCP/IP socket

sock = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
# host = input(str("Enter server address: "))
# Above line is for connecting to different computer on the same network
host = ip
server_address = (host, 10000)
print ('starting up on %s port %s' % server_address)
sock.connect(server_address)
print("Connection Successful\n")

sock.send(shost.encode())
sock_name = sock.recv(4096)
sock_name = sock_name.decode()
print(sock_name, "has joined")
print ("Waiting to recieve message")

while True:

    m=sock.recv(4096)
    m=m.decode()
    k=sock.recv(4096)
    k=k.decode()
    k=int(k)
    i=0
    a=""
    b=""
    f=random.randint(0,1)
    message=""
    while i!=k:
       
       
       f=random.randint(0,4)
       if(f==0):
          b="ACK Lost"
          print ("Faking ACK Loss") 
          message = sock.recv(4096)
          message = message.decode()
          sock.send(b.encode())
         
       else:
          b="ACK "+str(i)
          print ("Acking Sender Packet No." +str(i))
          message = sock.recv(4096)
          message = message.decode()
          
          sock.send(b.encode())
          a=a+message
          i=i+1
          
       
    print ('Received %s bytes from %s' % (len(message), sock_name))
    print (sock_name, ": ", m)


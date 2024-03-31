import time, socket, sys

#Karnvir Basra
#Arshpreet Dhillon 104932740

def dTB(n):  
    return n.replace("0b", "")

def bc(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(dTB(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

# Create a UDP Socket

sock = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 10000
sock.bind((host, port))
print(host, "(", ip, ")\n")
# name = input(str("Enter your name: "))
name = host
           
sock.listen(1)
print("\nWaiting to connect\n")
conn, addr = sock.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

sock_name = conn.recv(4096)
sock_name = sock_name.decode()
print(sock_name, "has connected")
conn.send(name.encode())


while True:
    message = input(str("Me : "))
    conn.send(message.encode())
    message=bc(message)
    f=str(len(message))
    conn.send(f.encode())
   
    i=0
    j=0
    j=int(input("N -> "))
    
   
    b=""
   
    j=j-1
    f=int(f)
    k=j
    while i!=f:
        
            conn.send(message[i].encode())
            b=conn.recv(4096)
            b=b.decode()
            print(b+ ": for Packet No." +(str(i)))
            if(b!="ACK Lost"):
                time.sleep(1)
                print("N is {"+(str(i))+" to "+str(k)+"} Sending next packet")
                i=i+1
                if:
                    k=i
                    k == i + j
                time.sleep(1)
            else:
                time.sleep(1)
                print("NACK'd! N{ "+(str(i))+" to "+str(k)+"} Resending Packet No. "+(str(i)))
                time.sleep(1)

          
     

# simple server UDP socket 
from socket import * 

host = '127.0.0.1'
port = 9999

server = socket(AF_INET, SOCK_DGRAM)
server.bind((host, port))

while True:
    
    message, addr = server.recvfrom(2048)
    message = message.decode()
    
    print(message)
    
    message = message.encode().upper()
    server.sendto(message, addr)


# simple client UDP socket 
from socket import *

host = "127.0.0.1"
port = 9999
addr = (host, port)

""" Creating the UDP socket """
client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Enter a word: ")

    if data == "exit":
        
        data = data.encode()
        client.sendto(data, addr)

        print("Disconneted from the server.")
        break

    data = data.encode()
    client.sendto(data, addr)

    data, addr = client.recvfrom(1024)
    data = data.decode()
    print("Server: ", data)

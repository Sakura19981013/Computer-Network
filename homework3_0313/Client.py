from socket import *

host = 'localhost'
port = 12356
buffsize = 2048

ADDR = (host,port)
tctimeClient = socket(AF_INET,SOCK_STREAM)
tctimeClient.connect(ADDR)

while True:
    data = input("Connected")
    if not data:
        break
    tctimeClient.send(data.encode())
    data = tctimeClient.recv(BUFFSIZE).decode()
    if not data:
        break
    print(data)
tctimeClient.close()
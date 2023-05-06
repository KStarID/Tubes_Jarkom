#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 5678
IP_ADDRESS = '127.0.0.1'
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print(f'Web server berjalan di {IP_ADDRESS}:{serverPort}')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Koneksi diterima dari {IP_ADDRESS}:{serverPort}')

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #request handler
        header = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send("HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #request handler
        header = "HTTP/1.1 404 not found\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send("HTTP/1.1 404 not found\nContent-Type: text/html\r\n\r\n".encode())
        print("404 Not Found")
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
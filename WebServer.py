#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 5500))
serverSocket.listen(1)
while True:
    print("Server is running")
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode('utf-8').strip("/")
        print(filename)
        f = open(filename)
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('404 Not Found'.encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close()

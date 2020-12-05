from socket import *
import random
serverName = 'localhost'
serverPort = 12000
serverAddress = (serverName, serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverAddress)
print('server is ready')
serverMessage = '1'.encode()


while True:
    clientMessage, clientAddress = serverSocket.recvfrom(1024)
    r = random.randint(0, 10)   # the server doesn't response some messages to imitate loss or drop
    if r%2 == 0:
        serverSocket.sendto(serverMessage, clientAddress)

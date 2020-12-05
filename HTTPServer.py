from socket import *
from server.ServerHandler import ServerHandler

serverName = 'localHost'
# serverPort = 80   # in case of using browser
serverPort = 8000    # in case of using client program
serverAddress = (serverName, serverPort)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)
serverHandler = ServerHandler()
serverSocket.listen(1)
print('web server is ready ')

while True:
    connectionSocket, addr = serverSocket.accept()
    GETMessage = connectionSocket.recv(1024).decode()   # receiving GET message
    print(GETMessage)
    requestedFileName = serverHandler.fileNameExtractor(GETMessage)
    requestedFile = serverHandler.getFile(requestedFileName)
    OKResponse = serverHandler.OKResponse(requestedFile)    # sending OK response
    connectionSocket.send(OKResponse)

from socket import *
import time

serverName = 'localhost'
serverPort = 12000
serverAddress = (serverName, serverPort)
pingSocket = socket(AF_INET, SOCK_DGRAM)
pingSocket.settimeout(1)


def ping(pingSocket, serverAddress):
    t1 = int(round(time.time() * 1000))
    pingSocket.sendto('ping'.encode(), serverAddress)   # sending the ping message
    try:
        serverMessage, add = pingSocket.recvfrom(1024)
        t2 = int(round(time.time() * 1000))
        print("RTT = " + str(t2 - t1))
    except:     # if no packet received after 1 sec, pingSocket throws exception and program will announce time out
        print('timeout')

    print('---------------------------------')


for i in range(10):
    ping(pingSocket, serverAddress)

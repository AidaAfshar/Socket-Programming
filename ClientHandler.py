class ClientHandler:
    def GETRequest(self, fileName, hostName):       # making the GET request with the given file name & host name
        requestMessage = "GET /" + fileName + " HTTP/1.1\n" + \
                         "Host:" + hostName + "\n" + \
                         "User-Agent: Aida as a client\n" + \
                         "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\n" + \
                         "Accept-Language: en-US,en;q=0.5\n" + \
                         "Connection: keep-alive\n"
        return requestMessage

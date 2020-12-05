import re


class ServerHandler:

    def getFile(self, fileName):
        try:
            with open("..\server's Database\\" + str(fileName), 'r') as file:   # openning the requested file & change it to string
                htmlFile = file.read()
        except:     # if no such file exist's, throw error
            with open("..\server's Database\errors\\404.html", 'r') as file:
                htmlFile = file.read()

        return htmlFile

    def OKResponse(self, file):

        responseMessage = "HTTP/1.1 200 OK\n" + \
                          "Connection: close\n" + \
                          "Content-Type: text/html\n" + \
                          "\n" + \
                          str(file)

        return responseMessage.encode()

    def fileNameExtractor(self, GETMessage):
        succesfull = re.search("GET /(.+?) HTTP/", str(GETMessage))     # extracting the file name from GET message
        fileName = ""
        if succesfull:
            fileName = succesfull.group(1)
        return fileName

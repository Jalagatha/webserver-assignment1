
from socket import *
from time import time, ctime

#specifying the server and the port to connect to
serverHostAddress = '127.0.0.1' 
serverPort = 12345

# Speciying the socket to use ipv4 and data gram based communication (UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

#specifying the timeout of the connection implemented on recv and accept for the clientSocket created
clientSocket.settimeout(1)

# loop to enable the Sending and receiving 10 
for i in range(10):
    startTime = time()  # Retrieve the current time
    message = "Ping " + str(i + 1) + " " + ctime(startTime)[11:19]

    try:
     
        clientSocket.sendto(message.encode(), (serverHostAddress, serverPort))
        encodedModified, serverAddress = clientSocket.recvfrom(1024)

        # Checking the current time 
        endTime = time()

        # Modified message is decoded.
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)

        # Prints the RTT
        print("Round Trip Time: %.3f ms" % ((endTime - startTime) * 1000))
    except timeout:
        print("PING %i Request timed out".center(30, "*") % (i + 1))

clientSocket.close()
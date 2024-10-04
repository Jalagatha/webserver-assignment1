# UDP server program.
from datetime import datetime
import random
from socket import *

# Create a UDP socket with a SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress  = '127.0.0.1'
ServerPort = 12345

# Assign IP address and port number to socket
serverSocket.bind((serverAddress, ServerPort))

# Get the assigned IP address and port number
ip_address, port = serverSocket.getsockname()
print(f"Server is running on IP address: {ip_address}, Port: {port}")


#create a loop to continously listen to client requests
while True:
	# Generate a random number between 0 and 10
	rand = random.randint(0, 10)

	# Receive the client packet together with its address
	message, address = serverSocket.recvfrom(1024)
	
    #Print a message indicating that a client has connected
	print(f"Received message from {address} : {message.decode()}")

	# if the random number generated is a multiple of 2, then the packet is considered lost and there is no need for a response
	if rand % 2 == 0:
		continue

	# send a response if otherwise
	serverSocket.sendto(message.upper(), address)
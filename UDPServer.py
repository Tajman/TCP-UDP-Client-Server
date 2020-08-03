# Tajour Cohen-Henry 
# CS 453 
# UDP Server code 

import re #imports regex
from socket import * 
serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_DGRAM) # creates socket 
serverSocket.bind(('', serverPort)) #binds server to the noted port which is 12000 in this case
print("The server is ready to receive") #waits for message from client 
############################################################################### 

#loop keeps connection alive
while True: 
	message, clientAddress = serverSocket.recvfrom(2048) #gets message 
	modifiedMessage = message.decode() #changes the byte message into a string
	matchedMess = re.match(r'(-|\s*)\d+\s*[\+,\-,\*\/]\s*(-*)\d+', modifiedMessage) #regex code to check if it is a valid message
	
#if the message is valid it evalualtes it to be sent back to the server with a status code 
#if it is not valid it sets the returning message to -1 with the error status code	
	if matchedMess is None: 
		newModifiedMessage = str(-1) 
		status = '300' 
		newModifiedMessage = ''.join([newModifiedMessage, status]) #joins both strings to make one message to send back 
		serverSocket.sendto(newModifiedMessage.encode(), clientAddress)
	else: 
		newModifiedMessage = str(eval(modifiedMessage)) 
		status = '200'
		newModifiedMessage = ''.join([newModifiedMessage, status]) #joins both strings to make one message to send back
		serverSocket.sendto(newModifiedMessage.encode(), clientAddress)

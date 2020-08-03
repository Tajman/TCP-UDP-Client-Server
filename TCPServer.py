# Tajour Cohen-Henry 
# CS 453 
# TCP Server code 

import re #imports regex
from socket import * 
serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_STREAM) # creates socket 
serverSocket.bind(('', serverPort)) #binds server to the noted port which is 12000 in this case
serverSocket.listen(1) #literaly listens for a single connection from the client to be made before it waits for a message
print('The server is ready to received') #waits for message from client 
#################################################################################### 

#loop keeps connection alive
while True: 
	connectionSocket, addr = serverSocket.accept() #accepts the message through the saved space made with listening for a connection space 
	sentence = connectionSocket.recv(1024).decode() #gets message and changes it to a string
	matchedMess = re.match(r'(-|\s*)\d+\s*[\+,\-,\*\/]\s*(-*)\d+', sentence) #regex code to check if it is a valid message 
	
#if the message is valid it evalualtes it to be sent back to the server with a status code 
#if it is not valid it sets the returning message to -1 with the error status code
	if matchedMess is None: 
		operationEquation = str(-1) 
		status = '300' 
		operationEquation = ''.join([operationEquation, status])#joins both strings to make one message to send back 
		connectionSocket.send(operationEquation.encode())
	else: 
		operationEquation = str(eval(sentence)) 
		status = '200'
		operationEquation = ''.join([operationEquation, status])#joins both strings to make one message to send back 
		connectionSocket.send(operationEquation.encode()) 
		
	connectionSocket.close() #closes the socket connection to make room for another one 
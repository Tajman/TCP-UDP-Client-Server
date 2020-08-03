# Tajour Cohen-Henry 
# CS 453 
# TCP Client code 

import re #imports regex
from socket import * 
serverName = '127.0.0.1' #IP for local host
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_STREAM) # creates socket
clientSocket.connect((serverName, serverPort)) #makes the connection to the server to this active socket
#########################################################################################

#user input
sentence = input('Enter a math expression (with +,-,*,/):') 
#sends message as bytes to the server port which is connected to the client
clientSocket.send(sentence.encode()) 
#after the server checks the message the client gets the message back
modifiedSentence = clientSocket.recv(1024) 
#########################################################################################  

#regex code to check if the returned message is valid or not
matchedValid = re.search(r'200$', modifiedSentence.decode()) 
matchedInvalid = re.search(r'300$', modifiedSentence.decode())  
#########################################################################################

#prints out final evalualated message depending if it is valid or not
if matchedInvalid: 
	inval = re.sub(r'300$', "", modifiedSentence.decode()) 
	print('From Server: ' + inval + '\nError: status code 300. Invalid entry') 
elif matchedValid:
	val = re.sub(r'200$', "", modifiedSentence.decode()) 
	print('From Server: ' + val + '\nCorrect: status code 200. Valid entry') 

clientSocket.close() #closes connection
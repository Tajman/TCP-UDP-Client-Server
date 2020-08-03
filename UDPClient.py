# Tajour Cohen-Henry 
# CS 453 
# UDP Client code 

import re #imports regex
from socket import * 
serverName = '127.0.0.1' #imports regex
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM) # creates socket 
######################################################################### 

#user input
message = input('Enter a math expression (with +,-,*,/):') 
#sends message as bytes to the server port which is connected to the client
clientSocket.sendto(message.encode(), (serverName, serverPort))  
#after the server checks the message the client gets the message back
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
########################################################################## 

#regex code to check if the returned message is valid or not
matchedValid = re.search(r'200$', modifiedMessage.decode()) #a message with a valid 200 status code 
matchedInvalid = re.search(r'300$', modifiedMessage.decode()) #a message with a valid 200 status code

#prints out final evalualated message depending if it is valid or not
if matchedInvalid: 
	inval = re.sub(r'300$', "", modifiedMessage.decode())
	print(inval + '\nError: status code 300. Invalid entry') 
elif matchedValid:
	val = re.sub(r'200$', "", modifiedMessage.decode())
	print(val + '\nCorrect: status code 200. Valid entry')
		
clientSocket.close() #closes connection

from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Ready to serve...")
#Fill in end

while True:
    # Establish the connection
    #fill in start 
    connectionSocket, addr = serverSocket.accept()
    #fill in end 
    
    try:
        message = connectionSocket.recv(1024).decode()
        
        if not message:
            # If message is empty, continue to the next connection
            connectionSocket.close()
            continue
        
        #fill in end
        print(f"Request received: {message}")
        
        if len(message.split()) < 2:
            # If the request does not contain enough parts, continue to the next connection
            connectionSocket.close()
            continue
        filename = message.split()[1]
        f = open(filename[1:])  # Remove the leading "/" from the filename
        #fill in start 
        outputdata =f.read() #fill in end 

        # Send HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())  # End of the response
        
        connectionSocket.close()
    
    except IOError:
        # Send a 404 Not Found response
        #Fill in start 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        #Fill in end 
        #Close client socket 
        #Fill in start
        connectionSocket.close()
        #Fill in close 

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding response


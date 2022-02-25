from socket import *
import base64

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = '\r\n My Message' 
    endmsg = '\r\n.\r\n' 

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    mailServer = 'localhost'
    mailPort = 80 #port number
    clientSocket = socket(AF_INET, SOCK_STREAM)#internet and socket protocols
    clientSocket.connect((mailServer, mailPort))
    # Fill in end

    recv = clientSocket.recv(1024)#client socket recieves certain amount of data
    print (recv) #print out the message
    if recv[:3] != '220': # if the message is not received
        print ('220 reply not received from server.')
    
    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n' 
    clientSocket.send(heloCommand) 
    recv1 = clientSocket.recv(1024)
    print (recv1)
    if recv1[:3] != '250': 
        print ('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    clientSocket.send('Mail FROM: <sp6750@nyu.edu>\r\n')
    recv1 = clientSocket.recv(1024)
    print (recv1)
    if recv1[:3] != '250': 
        print ('250 reply not received from server.')
    # Fill in end 

    # Send RCPT TO command and handle server response.
    # Fill in start
    clientSocket.send('RCPT TO: <sp6750@nyu.edu> \r\n')
    recv1 = clientSocket.recv(1024)
    print (recv1) 
    if recv1[:3] != '250': 
        print ('250 reply not received from server.')
    # Fill in end 

    # Send DATA command and handle server response.  
    # Fill in start 
    clientSocket.send('DATA\r\n') 
    recv1 = clientSocket.recv(1024)
    print (recv1)
    if recv1[:3] != '354': 
        print ('354 reply not received from server.')
    # Fill in end 

    # Send message data.
    # Fill in start 
    clientSocket.send('\r\n')
    clientSocket.send('something important\r\n')
    # Fill in end 

    # Message ends with a single period, sned message end and handle server response. 
    clientSocket.send('.\r\n')
    recv1 = clientSocket.recv(1024) 
    print (recv1) 
    if recv1[:3] != '250': 
        print ('250 reply not received from server.') 

    # Send QUIT command and handle server response.
    clientSocket.send('QUIT\r\n') 
    clientSocket.close() 
    pass

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

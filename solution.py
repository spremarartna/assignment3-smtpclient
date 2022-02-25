from socket import *
from xmlrpc import client


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = ('smtp.gmail.com', 465)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect((mailserver, 25))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    MAILFROMcommand = 'MAIL FROM: <alice@crepes.com>\r\n'
    clientSocket.send(MAILFROMcommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    RCPTTOcommand = 'RCPT TO: <bob@hamburger.com\r\n>'
    clientSocket.send(RCPTTOcommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    DATA = 'DATA\r\n'
    clientSocket.send(DATA.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4)
    if recv4[:3] != '354':
        print('354 reply not received from server. ')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    QUITcommand = 'QUIT\r\n'
    clientSocket.send(QUITcommand.encode())
    # Fill in end
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

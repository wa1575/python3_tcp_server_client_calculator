import socket
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating TCP socket
if not s.connect(('127.0.0.1',8089)):                # Connecting - IP : 127.0.0.1, PORT : 8089 
    print('Connected server!')
while 1: 
    message = input('input the command (q to quit, 0 to initialize) : ') # input
    if message=='q' or message=='Q':                         # if q or Q is exit
        break
    s.sendall(message.encode()) # ecnoding
    data = s.recv(1000)
    print('Recived', data.decode()) #decoding

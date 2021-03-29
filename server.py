import socket
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating TCP socket
s.bind(('127.0.0.1',8089))                           # Connecting - IP : 127.0.0.1, PORT : 8089 
s.listen(5)                                          # Can accept 5 clients

for i in range(0,5):                                 # 5 clients => 5 loop
    conn,addr = s.accept()                           # if client connecting
    print('connected client (ip,port)',addr)         # print the client info
    answer=0
    while 1:
        data = conn.recv(1024)                       # Formula received from client EX) 3 + 4 or  +6.
        data = data.decode()
        print(data)
        if not data:
            break
        number = []
        message=''
        if data[0]=='0':   # 0 is initialized
            answer=0       # forwad answer init
            message = 'first'
            print('answer = 0')
        elif data[0]=='+' or data[0]=='-' or data[0]=='*' or data[0]=='/': # If the data type is'+int'
            op=data[0] # by the operator
            if op=='+':
                message = 'answer : %d %s %d = %d' %(answer,op,int(data[1:]),answer+int(data[1:]))
                answer = answer+int(data[1:]) 
            elif op=='-':
                message = 'answer : %d %s %d = %d' %(answer,op,int(data[1:]),answer-int(data[1:]))
                answer = answer-int(data[1:])
            elif op=='*':
                message = 'answer : %d %s %d = %d' %(answer,op,int(data[1:]),answer*int(data[1:]))
                answer = answer*int(data[1:])
            elif op=='/':
                message = 'answer : %d %s %d = %d' %(answer,op,int(data[1:]),answer/int(data[1:]))
                answer = answer/int(data[1:])
            print(message)
        else: # normal Formula format ex) 1+1
            for i in range(0,len(data)): # loop in data len
                if data[i]=='+' or data[i]=='-' or data[i]=='*' or data[i]=='/': # check the operator
                    op=data[i] # save the operator
                    number.append(int(data[0:i]))  # Save number before operator
                    number.append(int(data[i+1:])) # Save number after operator
                    break
            if op=='+': # by the operator
                message = 'answer : %d %s %d = %d' %(number[0],op,number[1],number[0]+number[1])
                answer = answer+number[0]+number[1]
            elif op=='-':
                message = 'answer : %d %s %d = %d' %(number[0],op,number[1],number[0]-number[1])
                answer = answer+number[0]-number[1]
            elif op=='*':
                message = 'answer : %d %s %d = %d' %(number[0],op,number[1],number[0]*number[1])
                answer = answer+number[0]*number[1]
            elif op=='/':
                message = 'answer : %d %s %d = %d' %(number[0],op,number[1],number[0]/number[1])
                answer = answer+number[0]/number[1]
            print(message)
        conn.sendall(message.encode()) # answer encodeing 

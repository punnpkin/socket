import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 10080))

sock.listen(5)
print ('Server: ', sock.gethostbyname('localhost'),'is listening...')

mydict = dict()
mylist = list()

def tellOthers(enceptNum, whatToSay)
    for c in mylist:
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass

def subThreadIn(myconnection, connNumber):
    nickname = myconnection.recv(1024).decode()
    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('connection', connNumber, 'has nickname: ', nickname)
    tellOthers(connNumber, 'notice: '+mydict[connNumber]+' has joined')
    while True:
        try:
            recveMsg = myconnection.recv(1024).decode()
            if  recveMsg:
                print(mydict[connNumber], ' :', recveMsg)
                tellOthers(connNumber, mydict[connNumber]+' :'+recveMsg)
        
        except (OSError, ConnectionAbortedError)
            try:
                mydict.remove(myconnection)
            except:
                pass
            print(mydict[connNumber],'exit, ',len(mylist), ' person left')
            tellOthers(connNumber, 'notice: '+mydict[connNumber]+' has leaved')
            myconnection.close()
            return

while True:
    connction, addr = sock.accept()
    print('Accept a new connection', connection.getsockname(), connection.fileno())
    try:
        buf = connction.recv(1024).decode()
        if buf == '1':
            connction.send('welcome to server!')

            #new thread
            mythread = threading.Thread(target=subThreadIn, args=(connction, connction.fileno()))
            mythread.setDaemon(True)
            mythread.start()

        else:
            connction.send('please go out!')
            connction.close()
    
    except:
        pass

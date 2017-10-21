#!python2

content = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
<title>Hello</title>
</head>
<body>
It is from python! Num: %d
</body>
</html>
"""

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10080))
sock.listen(1) # don't queue up any requests
num=0
# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    num += 1
    req = csock.recv(1024) # get the request, 1kB max
    if 'GET' in req:
        csock.sendall( content % num)
    else:
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()

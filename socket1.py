#!python2

# Echo client program
import socket, sys

HOST = 'news.ustb.edu.cn'    # The remote host
PORT = 80                    # HTTP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall("GET / HTTP/1.0\r\n\r\n")
result = ""
while True:
    buf = s.recv(1024)
    if not buf:
        break
    result += buf
s.close()
print "%d bytes received" % len(result)
f = open("save.html", "w")
f.write(result)
f.close()

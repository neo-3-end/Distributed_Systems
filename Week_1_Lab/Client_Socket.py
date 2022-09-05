import socket

c = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

c.connect(('localhost', 6666))

c.sendall(b'Hello world')
data = c.recv(1024)

print('Received', repr(data))
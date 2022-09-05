import socket

c = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

c.connect(('localhost', 6666))
c.send(bytes('Hello', 'utf-8'))

with open('Client.txt', 'w') as f:
    while True:
        data = c.recv(2048)
        print(data)
        if not data:
            break
        f.write(data)
f.close()
c.close()

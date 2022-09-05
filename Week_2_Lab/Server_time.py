import socket
import time

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

s.bind(('localhost', 6666))
s.listen(5)
print("Waiting")
current_time = time.ctime(time.time())
while True:
    c_addr, c = s.accept()
    print(c_addr)
    data = c.recv(2000)
    print(data.decode())
    fn = open('Client.txt', "a")
    m = fn.read(2048)
    while (m):
        print(c.send(bytes(m), 'utf-8'))
    fn.close()

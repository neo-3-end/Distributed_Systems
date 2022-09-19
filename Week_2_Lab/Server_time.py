import socket
import time

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

s.bind(('localhost', 6969))
s.listen(5)
print("Waiting")
current_time = time.ctime(time.time())
while True:
    c_addr, c = s.accept()
    print(c_addr)
    data = c_addr.recv(1024)
    print(data.decode())
    file = open(data, 'w')
    file.write(current_time)
    file.close()
    c_addr.close()

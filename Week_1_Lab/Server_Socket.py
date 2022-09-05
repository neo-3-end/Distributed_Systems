import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

s.bind(('localhost', 6666))
s.listen(5)
print("Waiting")
c_addr, c = s.accept()
print(c_addr)
while True:
    data = c_addr.recv(1024)
    if not data:
        break
    c_addr.sendall(data)

import socket

s = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

s.bind(('localhost', 6969))
print('Waiting.....')
data, c_addr = s.recvfrom(1024)
print(data)
s.sendto(data, c_addr)

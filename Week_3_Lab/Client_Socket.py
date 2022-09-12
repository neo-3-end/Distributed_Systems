import socket

c = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
server_addr = ('localhost', 6969)
data = 'Hello World'
data_to_send = str.encode(data)
c.sendto(data_to_send, server_addr)
msg_from_server = c.recvfrom(1024)
msg = format(msg_from_server[0].decode())
print(msg)

import socket

c = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

c.connect(('localhost', 6969))
c.send(bytes('client.txt', 'utf-8'))
f = open('client.txt', 'r')
file_data = f.read()
data_to_write_in_file = file_data.encode()
new_f = open('server.txt', 'w')
new_f.write(data_to_write_in_file.decode())
new_f.close()
c.close()

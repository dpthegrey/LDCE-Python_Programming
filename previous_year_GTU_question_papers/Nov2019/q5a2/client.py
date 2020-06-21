import socket

# Creating Client socket
cs = socket.socket()

# Client will only connect to server
# takes (ip of server, port number which you have to connect with) as a single argument.
cs.connect(('localhost', 9999))

name = input('Enter your name ')
cs.send(bytes(name, 'utf-8'))

print(cs.recv(1024).decode())

import socket

# Creating Server Socket
ss = socket.socket()
print('Socket Created')

# Bind the address to socket (Only server will bind the socket to a port number)
ss.bind(('localhost', 9999))

# Listen for client request | listen() Takes number of client as argument
ss.listen(3)
print('waiting for connection')

while True:
    cs, addr = ss.accept()
    name = cs.recv(1024).decode()
    print(f"Connected with {name} at {addr} ")

    # server have to send byte format
    cs.send(bytes(f"Welcome to the server {name}", 'utf-8'))

    # Close the client socket
    cs.close()

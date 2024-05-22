"""Lab Objective: Create a login interface using sockets."""

import socket
print("Starting Client")
s = socket.socket()
s.connect(("127.0.0.1", 8084))
print("Connected to Server - Look at Wireshark")
s.recv(2048).decode()
s.recv(2048).decode()
print(s.recv(2048).decode())
s.send(input("").encode())
print(s.recv(2048).decode())
s.send(input("").encode())
print(s.recv(2048).decode())
s.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
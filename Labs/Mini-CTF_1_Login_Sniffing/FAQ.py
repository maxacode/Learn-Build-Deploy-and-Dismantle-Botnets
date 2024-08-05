"""Lab Objective: Create a login interface using sockets."""
"""

FAQ

Client wont Connect:
    1. Ensure IP/Port correct in Code
    2. Try another Port: 443, 8080, etc
    3. Try another network (Hotspot) 

No packets in wireshark:
    1. Ensure correct interface is setup.
    2. Filter based on Port of Socket


"""
import socket
print("Starting Client")
s = socket.socket()
# 172.20.2.254
# name: wifihacked - pass: helloworld
s.connect(("127.0.0.1", 8085))
print("Connected to Server")
print(1)
print(s.recv(2048).decode())
print(2)
print(s.recv(2048).decode())
print(3)
s.send(b"rockyou")
print(s.recv(2048).decode())
print(4)
print(s.recv(2048).decode())
print(5)
s.send(input("").encode())
print(6)
print(s.recv(2048).decode())
print(7)
s.send(input("").encode())
print(s.recv(2048).decode())
s.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution

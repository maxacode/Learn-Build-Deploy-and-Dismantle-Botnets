# Client Code:
import socket
print("starting client")
new_socket = socket.socket()
new_socket.connect(("0.0.0.0", 50001))
data = new_socket.recv(2048).decode()
print(data)
new_socket.close()  

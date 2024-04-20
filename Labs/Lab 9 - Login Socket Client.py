"""
Send Welcome message to Client
Server Ask Client for Username
Client sends username
Server asks for password
Client Sends password
Server compares Username & Password to Known Credentials and Authenticates
If correct Credentials Servers says “Welcome User”
If wrong, Server tells client “Wrong Credentials”


"""

import socket

def client():
    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Receive welcome message
    print(client_socket.recv(1024).decode())

    # Send username
    username = input("Username: ")
    client_socket.sendall(username.encode())

    # Send password
    password = input("Password: ")
    client_socket.sendall(password.encode())

    # Receive authentication result
    response = client_socket.recv(1024).decode()
    print(response)

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client()

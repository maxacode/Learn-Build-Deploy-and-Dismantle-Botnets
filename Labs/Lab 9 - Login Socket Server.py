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
# SERVER 
import socket
port = 12347
def server():
    # Known username and password
    USERNAME = 'admin'
    PASSWORD = 'password'

    # Set up the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(10)
    print("Server is waiting for client connection...")

    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Send welcome message
    client_socket.sendall(b"Welcome to the server! Please log in.")

    # Ask for username
   # client_socket.sendall(b"Enter your username:")
    username = client_socket.recv(1024).decode()

    # Ask for password
   # client_socket.sendall(b"Enter your password:")
    password = client_socket.recv(1024).decode()
    import os
    # Authenticate user
    if username == USERNAME and password == PASSWORD:
        client_socket.sendall(b"Welcome, Authentication Valid, send a CMD Command")
        import subprocess
        cmdFromClient = client_socket.recv(1024).decode()
        cmd = subprocess.check_output(cmdFromClient, shell=False)
        client_socket.sendall(bytes(cmd))

    else:
        client_socket.sendall(b"Invalid username or password")

    # Close connection
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    server()

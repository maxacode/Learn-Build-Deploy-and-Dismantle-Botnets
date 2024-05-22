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
# CLIENT 
import socket
port = 12347
def client():
    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', port))

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
    if "Welcome" in response:
        print(response)
        client_socket.sendall(input("Enter cmd here: ").encode())
        response2 = client_socket.recv(1024).decode()
        print(response2)
        

    else:
        print(response)


    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client()

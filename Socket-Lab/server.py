# Server Code:
import socket
print("starting Server")
new_socket = socket.socket()
new_socket.bind(("0.0.0.0", 50001))
new_socket.listen(4)
conn, addr = new_socket.accept()
print(conn,addr)
conn.send("Hello from the other side".encode())
new_socket.close()



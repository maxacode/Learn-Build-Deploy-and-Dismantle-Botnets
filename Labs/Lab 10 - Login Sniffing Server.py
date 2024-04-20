"""Lab Objective: Create a login interface using sockets."""
import socket
import hashlib
import os, sys
# function 
hash = "f806fc5a2a0d5ba2471600758452799c"        

password = "28eed053fa28fe8e5a9f59eb925c090b"
port = 8084
while True: 
    try:

        print("Starting Server")
        s = socket.socket()
        print(port)
        s.bind(("0.0.0.0", port))
        s.listen(30)
        conn, addr = s.accept()
        print(addr)
        conn.send("database of users| username: bWFrcwo= password: aXN0aGViZXN0Cg==".encode()) #S1

        conn.send(f"Send the server a message with the plain text value of: {hash} ".encode()) #s2

        hashVerify = conn.recv(2048).decode() #r3

        print(hashVerify)

        hashFromUser = hashlib.md5(hashVerify.encode('utf-8')).hexdigest()

        #print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())



        if hashFromUser != hash:
            conn.send("Invalid Plain Text".encode())#S4
            conn.close()
        else:
            conn.send("Correct hash".encode())#S4
 
        conn.send(" Welcome to the server!\nPlease insert your Username:".encode())#s5

        username = conn.recv(2048).decode()#r6
        print(username)
        conn.send("Please insert the Password:".encode())#s7

        passwordUser = conn.recv(2048).decode()#r8
        print(passwordUser)
        passwordUser2 = hashlib.md5(passwordUser.encode('utf-8')).hexdigest()

        if username == "maks" and passwordUser2 == password:
            conn.send(f"Welcome {username} the flag is: WW91QXJlVGhlQmVzdCEK".encode())
        else:
            conn.send("Wrong username or password".encode())

        s.close()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        port += 1 
        pass

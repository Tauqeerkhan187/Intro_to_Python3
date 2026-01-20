import socket

# HOST = '142.250.66.110'
# PORT = 80

HOST = '127.0.0.1'
PORT = 21001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")
    
    # receive assigned client ID
    first_msg = s.recv(4096)
    if not first_msg:
        print("Server disconnected immediately")
    else:
        print("Server:", first_msg.decode())

    while True:
        message = input("Enter message: ")
        # message = "exit"
        s.send((message).encode())

        message_received = ""
        data = s.recv(32768)
        if not data:
            print("Server disconnected")
            break
        
        message_received = data.decode()
        print("Server answer: ", message_received)

        print("Server answer: ", message_received)

print("Client finished")
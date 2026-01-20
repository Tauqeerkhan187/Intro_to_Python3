import socket
from threading import Thread, Lock

HOST = '0.0.0.0'
PORT = 21001
s = None

connected_clients_number = 0

# global
lock = Lock()
new_client_id = 1
clients = {} # client_id = conn
messages = [] # list of dicts: id, text, need_to_send


def get_undelivered_for(client_id):
    """Collecct all messages pending for client_id and mark them delivered."""
    
    collected = []
    for m in messages:
        
        if client_id in m["need_to_send"]:
            collected.append(f'from {m["from"]} : {m["text"]}')
            m["need_to_send"].remove(client_id)
    return collected
            
def client_processor(conn, client_id):
    
    global connected_clients_number

    while True:
        data = conn.recv(4096)
        if not data:
            print(f"Client {client_id} disconnected")
            with lock:
                connected_clients_number -= 1
                if client_id in clients:
                    del clients[client_id]
            break

        message_received = data.decode()

        print("Received message from client: ", message_received)
        
        # Store incoming message with need_to_send = all other connected client ids
        with lock:
            other_ids = [cid for cid in clients.keys() if cid != client_id]
            messages.append({
                "from": client_id,
                "text": message_received,
                "need_to_send": other_ids
            })
            
        with lock:
            pending = get_undelivered_for(client_id)
            
        if pending:
            reply = "\n".join(pending)
        else:
            reply = "No new messages available!"
            
        conn.send(reply.encode())
        

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)

while True:
    conn, addr = s.accept()
    
    with lock:
        client_id = new_client_id
        new_client_id += 1
        
        clients[client_id] = conn
        connected_clients_number += 1
        
    print(f"Client connected from address: {addr}, assigned ID: {client_id}")
    
    # tell client its ID once on connect
    conn.send(f"Your client ID is {client_id}".encode())
    
    client_thread = Thread(target=client_processor, args=(conn, client_id))
    client_thread.start()

s.close()
print("Server finished")

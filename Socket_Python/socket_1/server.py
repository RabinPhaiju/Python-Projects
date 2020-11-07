import socket
import threading

HEADER = 64 # 64 bytes
PORT = 5050
SERVER = '192.168.254.3'
SERVER = socket.gethostbyname(socket.gethostname()) # get your IPV4 ip address # use public address to run the client server across the internet
HOSTNAME = socket.gethostname() # get your comp name
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
server.bind(ADDRESS) # bind socket with address


def handle_client(conn, addr): # handle individual client btwn server
    # it is in own thread
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # how big the msge is it will be 64 bytes in a connection
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}, {msg}]')
            conn.send(f"Msg Received [{msg}]".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept() # when new connection ocuur and save to conn, addr
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        # new client = new thread, start function thread is already running so sub 1


print('[STARTING] server is starting...')
start()


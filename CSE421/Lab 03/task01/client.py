import socket

HEADER = 64
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
DISCONNECT_MSG = "End"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # Padding
    send_length += b" " * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


msg = f"The hostname of client is {socket.gethostname()} and the IP address is {SERVER}"

send(msg)
send(DISCONNECT_MSG)

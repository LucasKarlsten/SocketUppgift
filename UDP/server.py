import socket


class ChatRoom:
    def __init__(self, host, port):
        # Initiera en ny klass med host och port, sätter också upp en ny lista med cliens
        self.host = '127.0.0.1'
        self.port = 22322
        self.clients = []
        # Upprättar en socket som använder Ipv4 och som kommer skicka data över UDP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
# HOST = '127.0.0.1'
# PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((ChatRoom.host, ChatRoom.port))
    print(f'Server listening on adress; {ChatRoom.host} : {ChatRoom.port}')

    while True: 
        data, addr = sock.recvfrom(256)
        print(f'Message recieved from {addr}')

        data_decoded = data.decode('utf-8')
        response = f'echo, {data_decoded}'
        sock.sendto(response.encode('utf-8'), addr)


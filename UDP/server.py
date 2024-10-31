import socket

class ChatRoom:
    # Skapar en klass med en konstruktor och ger den host, port, server socketen, och en set() för klienter
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = set()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        try:
            # Programmet binder sig till den deklarerade porten och ip-adressen
            self.server_socket.bind((self.host, self.port))
            print(f"Server upprättad på {self.host}:{self.port}")
            while True:
                # Servern tar emot data och adresser som kommer från klienterna
                data, addr = self.server_socket.recvfrom(1024)
                # Om klienten inte redan är "registrerad" i set()en med clients så printar den ut att en ny har joinat"
                if addr not in self.clients:
                    self.clients.add(addr)
                    print(f"New client connected: {addr}")
                
                # Decodea meddelandet med utf8 och printar på servern
                message = data.decode("utf-8")
                print(f"Message received from {addr}: {message}")
                
                # Skicka meddelandet till alla klienter, utom den som skickade
                for client in self.clients:
                    if client != addr:
                        self.server_socket.sendto(data, client)
                        
        except Exception as e:
            print(f"Ett fel uppstod: {e}")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    chat_room = ChatRoom(HOST, PORT)
    chat_room.start()

import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def send_messages(sock):
    # Funktion för att skicka meddelanden
    while True:
        message = input("Enter message: ")
        # Encodear meddelanet och skickar till servern 
        sock.sendto(message.encode('utf-8'), (HOST, PORT))
        print(f"Sent: {message}")

def receive_messages(sock):
    # Funktion för att ta emot meddelanden
    while True:
        try:
            # Tar emot och decodear meddelandet från adressen
            data, addr = sock.recvfrom(1024)
            print(f"\nReceived from {addr}: {data.decode('utf-8')}")
        except Exception as e:
            print(f"Error in receive thread: {e}")
            break

# Skapa en UDP socket (Ipv4)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
    print(f"Connecting to server at {HOST}:{PORT}")
    
    # Skapar två threads, en för att att skicka och en för att ta emot meddelanden
    # Ger den en target, som är "vad" som ska göras och args är argumentet för targetens funktion
    send_thread = threading.Thread(target=send_messages, args=(client_sock,))
    receive_thread = threading.Thread(target=receive_messages, args=(client_sock,))
    
    # Därefter starta båda threadsen
    send_thread.start()
    receive_thread.start()
    
    # Och sen join, som väntar på att båda threadsen är klara 
    send_thread.join()
    receive_thread.join()

print("Disconnected from server.")
import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
    message = f'Hello from the other side!'
    encoded_message = message.encode('utf-8')

    client_sock.sendto(encoded_message, (HOST, PORT))
    response, addr = client_sock.recvfrom(256)
    decode_message = response.decode('utf-8')

    print(f'Message recieved from server {decode_message}')
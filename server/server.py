import socket
from screenshot import Screenshot

HOST = "127.0.0.1"
PORT = 8000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen(1)
            print("Waiting for client connection...")

            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection established with {client_address}")

                client_socket.recv(1024)
                client_socket.send(b'OK')

                while True:
                    image_data = Screenshot()

                    for i in range(len(image_data) // 1024 + 1):
                        input_bytes = image_data[i * 1024 : i * 1024 + 1024]
                        client_socket.send(input_bytes)

                    client_socket.send(bytes(1024))

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_server()

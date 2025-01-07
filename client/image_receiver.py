import socket
import pygame
import io
import threading

HOST = "127.0.0.1"
PORT = 8000 
photo = bytearray()
photo_lock = threading.Lock()

def receive_images(screen, WIDTH, HEIGHT):
    global photo
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.connect((HOST, PORT))
            
            server_socket.send(b'CONNECTED')
            server_socket.recv(1024)
            
            print("Connected to server. Waiting for images...")

            while True:
                pkg_photo = server_socket.recv(1024)
                
                if not pkg_photo:
                    break

                if pkg_photo == bytes(1024): 
                    with photo_lock:
                        if photo:
                            try:
                                image_file = io.BytesIO(photo)
                                image = pygame.image.load(image_file)
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                screen.blit(image, (0, 0))
                            except pygame.error as e:
                                print("Error loading image:", e)

                            photo = bytearray()
                else:
                    with photo_lock:
                        photo.extend(pkg_photo)

        except Exception as e:
            print(f"Error: {e}")

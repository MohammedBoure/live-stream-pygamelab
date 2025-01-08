import pygame
import threading
from .image_receiver import receive_images

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def start(WIDTH=800,HEIGHT=600,HOST="127.0.0.1", PORT=8000):
    receiver_thread = threading.Thread(target=receive_images, args=(screen, WIDTH, HEIGHT,HOST,PORT), daemon=True)
    receiver_thread.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    start()

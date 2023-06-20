import pygame
import numpy as np

GREEN = (0, 146, 70)
WHITE = (255, 255, 255)
RED = (206, 43, 55)
pygame.init()

width, height = 600, 400


screen = pygame.display.set_mode((width, height))


rotated_surface = pygame.Surface((height, width))

rotated_surface.fill(WHITE)

green_height = width // 3
pygame.draw.rect(rotated_surface, GREEN, (0, 0, height, green_height))

white_height = green_height
pygame.draw.rect(rotated_surface, WHITE, (0, green_height, height, white_height))


red_height = green_height
pygame.draw.rect(rotated_surface, RED, (0, green_height * 2, height, red_height))

rotated_surface = pygame.transform.rotate(rotated_surface, 90)

screen.blit(rotated_surface, (0, 0))

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

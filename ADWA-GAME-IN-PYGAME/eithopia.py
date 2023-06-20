import pygame
import math

GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
pygame.init()

width, height = 600, 400

screen = pygame.display.set_mode((width, height))

screen.fill(WHITE)


stripe_height = height // 3


pygame.draw.rect(screen, GREEN, (0, 0, width, stripe_height))

pygame.draw.rect(screen, YELLOW, (0, stripe_height, width, stripe_height))


pygame.draw.rect(screen, RED, (0, stripe_height * 2, width, stripe_height))

circle_radius = stripe_height // 2
circle_center = (width // 2, height // 2)
pygame.draw.circle(screen, BLUE, circle_center, circle_radius)


star_radius = circle_radius * 0.4
star_points = []
for i in range(10):
    angle = 2 * 3.14159 * i / 10 - 3.14159 / 2
    if i % 2 == 0:
        x = circle_center[0] + int(star_radius * 0.5 * math.cos(angle))
        y = circle_center[1] - int(star_radius * 0.5 * math.sin(angle))
    else:
        x = circle_center[0] + int(star_radius * math.cos(angle))
        y = circle_center[1] - int(star_radius * math.sin(angle))
    star_points.append((x, y))

pygame.draw.polygon(screen, YELLOW, star_points)


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

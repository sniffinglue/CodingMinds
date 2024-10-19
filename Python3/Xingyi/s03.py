import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Draw a rectangle based on a key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Draw a green rectangle at a random position
                pygame.draw.rect(screen, (0, 255, 0), (random.randint(1, 400), random.randint(1, 450), 100, 50))
            elif event.key == pygame.K_DOWN:
                pygame.draw.rect(screen, (255, 0, 0), (random.randint(1, 400), random.randint(1, 450), 50, 50))
            elif event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, (0, 0, 255), (random.randint(1, 400), random.randint(1, 450), 70, 50))
            elif event.key == pygame.K_RIGHT:
                pygame.draw.rect(screen, (255, 255, 255), (random.randint(1, 400), random.randint(1, 450), 45, 50))
    
    pygame.display.update()
    clock.tick(60)

import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600

pygame.display.set_caption("Minesweeper")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#3C3F41")

    # RENDER YOUR GAME HERE

    pygame.display.flip()

pygame.quit()

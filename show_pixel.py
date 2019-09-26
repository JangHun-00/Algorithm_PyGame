import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW_BRIGHT = (255, 255, 224)

size = (1300, 600)
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("Show pixel")
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill(YELLOW_BRIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, BLACK, (0, 300, 80, 30))
    pygame.draw.rect(screen, BLACK, (1220, 300, 80, 30))
    for i in range(10):
        pygame.draw.rect(screen, BLACK, (80+i*116, 252, 96, 96), 10)
    for j in range(9):
        pygame.draw.rect(screen, BLACK, (80+j*129.5, 247.75, 104.5, 104.5), 10)
    for k in range(8):
        pygame.draw.rect(screen, BLACK, (80+k*146.25, 241.875, 116.25, 116.25), 10)
    for k in range(7):
        pygame.draw.rect(screen, BLACK, (80+k*167.85, 233.575, 132.85, 132.85), 10)
    pygame.display.update()

pygame.quit()
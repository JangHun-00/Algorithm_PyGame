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

    pygame.draw.rect(screen, BLACK, (0, 300, 200, 30))
    pygame.draw.rect(screen, BLACK, (1100, 300, 200, 30))
    for i in range(4):
        pygame.draw.rect(screen, BLACK, (200 + i * 247.5, 225, 157.5, 157.5), 10)

    pygame.display.update()

pygame.quit()
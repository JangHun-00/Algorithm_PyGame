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

    pygame.draw.rect(screen, BLACK, (0, 300, 300, 30))
    pygame.draw.rect(screen, BLACK, (1000, 300, 300, 30))
    for i in range(3):
        pygame.draw.rect(screen, BLACK, (300 + i * 275, 225, 150, 150), 10)

    pygame.display.update()

pygame.quit()
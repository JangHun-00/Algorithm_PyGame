import pygame
import sys
import random

pygame.init()

class Block:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        if self.num < other.num:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.num > other.num:
            return True
        else:
            return False

    def __le__(self, other):
        if self.num <= other.num:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.num >= other.num:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num != other.num
            return True
        else:
            return False

    def draw(self, color=BLACK, index, total_length):
        global size
        # 앞 뒤로 80px 남기고, 칸 별로 최소 간격 20px
        # 계산 공식: (1140 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
        # 10개 일 때, 칸: 96px, 간격: 20px
        # 9개 일 때, 칸: 104.5px, 간격: 25px
        # 8개 일 때, 칸:
        position = (80, size[0]-80, (size[1] / 2) - (rect_size / 2))
        pygame.


def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))


def writeText(text, x, y):
    textfont = pygame.font.Font('D2CodingBold-Ver1.3.2-20180524.ttf', 15)
    text = textfont.render("{}".format(text), True, (0, 0, 0))
    drawObject(text, x, y)


def createButton(color, x, y, width, height, line=0):
    global screen
    pygame.draw.rect(screen, Dark[color], (x, y, width, height), line)
    mouse = pygame.mouse.get_pos()
    if (x < mouse[0] < x+width) and (y < mouse[1] < y + height):
        pygame.draw.rect(screen, color, (x, y, width, height), line)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW_BRIGHT = (255, 255, 224)

Dark = {
    RED: (200, 0, 0),
    GREEN: (0, 200, 0),
    BLUE: (0, 0, 200),
}

size = (1300, 600)
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("Learning Algorithm")

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


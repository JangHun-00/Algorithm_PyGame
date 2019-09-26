import pygame
import sys
import random

pygame.init()

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

def drawObject(obj, x, y):
    global screen
    screen.blit(obj, (x, y))


def writeText(text, x, y, font, size, color=(0, 0, 0)):
    if font == 'D2':
        textfont = pygame.font.Font('D2CodingBold-Ver1.3.2-20180524.ttf', size)
    elif font == '도현':
        textfont = pygame.font.Font('배달의민족_도현.ttf', size)

    text = textfont.render("{}".format(text), True, color)
    drawObject(text, x, y)


def createButton(color, x, y, width, height, line=0):
    global screen
    pygame.draw.rect(screen, Dark[color], (x, y, width, height), line)
    mouse = pygame.mouse.get_pos()
    if (x < mouse[0] < x+width) and (y < mouse[1] < y + height):
        pygame.draw.rect(screen, color, (x, y, width, height), line)


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
        if self.num != other.num:
            return True
        else:
            return False

    def draw(self, index, total_length, color=BLACK):
        global size
        # 앞 뒤로 80px 남기기
        # 계산 공식: (1140 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
        # 10개 일 때, 칸: 96px, 간격: 20px, 시작 y: 252px
        # 9개 일 때, 칸: 104.5px, 간격: 25px, 시작 y: 247.75px
        # 8개 일 때, 칸: 116.25px, 간격: 30px, 시작 y: 241.875px
        # 7개 일 때, 칸: 132.85px, 간격: 35px, 시작 y: 233.575px

        # 앞 뒤로 150px 남기기
        # 계산 공식: (1000 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
        # 6개 일 때, 칸: 137.5px, 간격: 35px, 시작 y: 231.25px
        # 5개 일 때, 칸: 148px, 간격: 65px, 시작 y: 226px

        # 앞 뒤로 200px 남기기
        # 계산 공식: (900 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
        # 4개 일 때, 칸: 150px, 간격: 100px, 시작 y: 225px

        # 앞 뒤로 300px 남기기
        # 계산 공식: (700 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
        # 3개 일 때, 칸: 150px, 간격: 125px, 시작 y: 225px


def select_length():
    while True:
        clock.tick(30)
        screen.fill(YELLOW_BRIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


while True:
    clock.tick(30)
    screen.fill(YELLOW_BRIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()
pygame.quit()


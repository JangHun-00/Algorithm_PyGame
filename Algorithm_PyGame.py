import pygame
import sys
import random
import copy


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
YELLOW_BRIGHT = (255, 255, 224)
GREY = (169, 169, 169)

Dark = {
    RED: (200, 0, 0),
    GREEN: (0, 200, 0),
    BLUE: (0, 0, 200),
    YELLOW: (200, 200, 0),
}

size = (1300, 600)
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("Learning Algorithm")

clock = pygame.time.Clock()


def writeText(text, x, y, size, font='D2', color=BLACK, rect=None):
    """
    텍스트를 스크린에 그리는 함수

    :param text: 쓰고 싶은 문자열
    :param x: 텍스트 x 좌표
    :param y: 텍스트 y 좌표
    :param size: 텍스트 사이즈
    :param font: 텍스트 폰트(D2, 도현)
    :param color: 텍스트 색깔
    :param rect: x, y가 좌측 상단일 경우는 None, 중심일 경우는 center
    """
    if font == 'D2':
        textfont = pygame.font.Font('D2CodingBold-Ver1.3.2-20180524.ttf', size)
    elif font == '도현':
        textfont = pygame.font.Font('배달의민족_도현.ttf', size)

    text = textfont.render("{}".format(text), True, color)

    if rect == 'center':
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    else:
        screen.blit(text, (x, y))


def createButton(color, x, y, width, height, line=0):
    """
    버튼을 그리는 함수

    :param color: 버튼 색깔
    :param x: 버튼 x 좌표
    :param y: 버튼 y 좌표
    :param width: 버튼 가로 길이
    :param height: 버튼 세로 길이
    :param line: 버튼 외곽에 선을 추가할거면 line 변수에 int 입력
    """
    global screen
    pygame.draw.rect(screen, Dark[color], (x, y, width, height), line)
    mouse = pygame.mouse.get_pos()
    if (x < mouse[0] < x+width) and (y < mouse[1] < y + height):
        pygame.draw.rect(screen, color, (x, y, width, height), line)


def checkBlock(total_list):
    """
    리스트 내 블록 갯수에 따라 블록 크기를 결정하는 함수

    :param total_list: Block이 들어있는 리스트
    :return: start_x(왼쪽 공백 길이), start_y(시작 y 좌표),
             block_size(양 공백과 블록 간 공백을 제외한 나머지 길이를 균등하게 나눈 값), blank(블록 간 공백)
    """
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

    total_length = len(total_list)

    if 7 <= total_length <= 10:
        start_x = 80
        if total_length == 10:
            blank = 20
        elif total_length == 9:
            blank = 25
        elif total_length == 8:
            blank = 30
        elif total_length == 7:
            blank = 35

    elif 5 <= total_length <= 6:
        start_x = 150
        if total_length == 6:
            blank = 35
        elif total_length == 5:
            blank = 65

    elif total_length == 4:
        start_x = 200
        blank = 100

    elif total_length == 3:
        start_x = 300
        blank = 125

    else:
        raise ValueError

    block_size = ((size[0] - (start_x * 2)) - (blank * (total_length - 1))) / total_length
    start_y = ((size[1] / 2) - (block_size / 2))
    return (start_x, start_y, block_size, blank)


def drawBlock(total_list, color=BLACK, line=10):
    """
    리스트 길이에 맞는 블록 크기를 구하고, 리스트 내 각 블록들을 draw 메서드를 통해 크기에 맞게 스크린에 그려주는 함수

    :param total_list: 블록이 들어있는 리스트
    :param color: 블록 색깔
    :param line: 블록 겉테두리(숫자는 두께)
    """
    (start_x, start_y, block_size, blank) = checkBlock(total_list)
    for i, block in enumerate(total_list):
        block_info = ((start_x)+i*(block_size+blank), start_y, block_size, block_size)
        block.draw(block_info, color, line)

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

    def __str__(self):
        return "{}".format(self.num)

    def __int__(self):
        return self.num

    def __float__(self):
        return self.num

    def __repr__(self):
        return "{}".format(self.num)

    def draw(self, info, color=BLACK, line=10):
        """
        개별 블록을 직접 그리는 메서드

        :param info: 블록이 그려져야할 좌표값(x좌표=info[0], y좌표=info[1])과 블록 사이즈(info[2]), 각 블록 간 공백(info[3])
        :param color: 블록 색깔
        :param line: 블록 테두리
        """
        pygame.draw.rect(screen, color, info, line)
        num_font = pygame.font.Font('D2CodingBold-Ver1.3.2-20180524.ttf', round(info[2]/2)) # 폰트 크기 = (블록 사이즈 / 2)
        num_text = num_font.render("{}".format(self.num), True, color) # 화면에 그릴 글자는 개별 블록의 숫자
        num_text_rect = num_text.get_rect(center=(round((2*info[0]+info[2])/2), round((2*info[1]+info[3])/2))) # 블록 중앙
        screen.blit(num_text, num_text_rect)


def select_length():
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def show_bubble(data_list):
    # 버블정렬을 화면에 그리는 총괄 함수
    global index, bubble_process
    index = 0
    bubble_process = bubble_result(data_list)
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        bubble_process[index][0](bubble_process[index][1], bubble_process[index][2])
        pygame.display.update()


def bubble_result(data_list):
    # 버블 정렬의 순차 과정을 담은 리스트를 return(인덱스 0: 함수 이름, 1: 블록들이 담긴 리스트, 2: tmp(현재 비교 대상)
    global index, bubble_process
    result = []
    for check in range(len(data_list)-1, 0, -1):
        for i in range(check):
            tmp_list = copy.deepcopy(data_list)
            result.append((bubble_draw, tmp_list, i))
            if data_list[i] > data_list[i+1]:
                tmp_list2 = copy.deepcopy(data_list)
                result.append((bubble_change, tmp_list2, i))
                temp = data_list[i]
                data_list[i] = data_list[i+1]
                data_list[i+1] = temp
    return result


def bubble_draw(data_list, tmp, color=BLACK, line=10):
    # 버블 정렬 중, 기본 상태를 그리는 함수
    global index, bubble_process
    (start_x, start_y, block_size, blank) = checkBlock(data_list)
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)
        done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT:
                    if index > 0:
                        index -= 1
                        done = True

                elif event.key == pygame.K_RIGHT:
                    if index < len(bubble_process) - 1:
                        index += 1
                        done = True

        writeText('Bubble Sort(버블 정렬)', 20, 20, 30, '도현')

        for i, block in enumerate(data_list):
            block_info = ((start_x)+i*(block_size+blank), start_y, block_size, block_size)
            block.draw(block_info, color, line)
            if i == tmp:
                writeText('{} vs {} 비교'.format(data_list[i].num, data_list[i+1].num), 650, 150, 40, '도현', BLACK, 'center')

                red_box1 = pygame.Rect((start_x)+i*(block_size+blank)-20, start_y+block_size+30, block_size+40, 10)
                red_box2 = pygame.Rect((start_x)+(i+1)*(block_size+blank)-20, start_y+block_size+30, block_size+40, 10)
                down_red1 = pygame.Rect((0, 0), (10, round(block_size/2)))
                down_red1.center = red_box1.center
                down_red1.top = red_box1.top
                down_red2 = pygame.Rect((0, 0), (10, round(block_size/2)))
                down_red2.center = red_box2.center
                down_red2.top = red_box2.top
                down_red3 = pygame.Rect(down_red1.left, down_red1.bottom-10, down_red2.right - down_red1.left ,10)
                pygame.draw.rect(screen, RED, red_box1)
                pygame.draw.rect(screen, RED, red_box2)
                pygame.draw.rect(screen, RED, down_red1)
                pygame.draw.rect(screen, RED, down_red2)
                pygame.draw.rect(screen, RED, down_red3)
        pygame.display.update()
        if done == True:
            break


def bubble_change(data_list, tmp, color=BLACK, line=10):
    # 버블 정렬 중, 두 값이 교체되는 경우를 그리는 함수
    global index, bubble_process
    (start_x, start_y, block_size, blank) = checkBlock(data_list)
    front_x = (start_x)+tmp*(block_size+blank)
    back_x = (start_x)+(tmp+1)*(block_size+blank)
    distance = back_x - front_x
    move = 5

    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)
        done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT:
                    if index > 0:
                        index -= 1
                        done = True
                elif event.key == pygame.K_RIGHT:
                    if index < len(bubble_process) - 1:
                        index += 1
                        done = True

        writeText('Bubble Sort(버블 정렬)', 20, 20, 30, '도현')

        for i, block in enumerate(data_list):
            if i == tmp or i == tmp + 1:
                if move > distance:
                    move = distance

                if i == tmp:
                    writeText('{} > {} 이므로 작은 값이 앞으로 오도록 교체'.format(data_list[i].num, data_list[i + 1].num), 650, 150, 40, '도현', BLACK, 'center')
                    red_box1 = pygame.Rect((start_x) + i * (block_size + blank) - 20, start_y + block_size + 30,
                                           block_size + 40, 10)
                    red_box2 = pygame.Rect((start_x) + (i + 1) * (block_size + blank) - 20, start_y + block_size + 30,
                                           block_size + 40, 10)
                    down_red1 = pygame.Rect((0, 0), (10, round(block_size / 2)))
                    down_red1.center = red_box1.center
                    down_red1.top = red_box1.top
                    down_red2 = pygame.Rect((0, 0), (10, round(block_size / 2)))
                    down_red2.center = red_box2.center
                    down_red2.top = red_box2.top
                    down_red3 = pygame.Rect(down_red1.left, down_red1.bottom - 10, down_red2.right - down_red1.left, 10)
                    pygame.draw.rect(screen, RED, red_box1)
                    pygame.draw.rect(screen, RED, red_box2)
                    pygame.draw.rect(screen, RED, down_red1)
                    pygame.draw.rect(screen, RED, down_red2)
                    pygame.draw.rect(screen, RED, down_red3)

                    block_info = (
                    (start_x) + (i + 1) * (block_size + blank) - distance, start_y, block_size, block_size)
                    block.draw(block_info, color, line)
                elif i == tmp + 1:
                    block_info = (
                    (start_x) + (i - 1) * (block_size + blank) + distance, start_y, block_size, block_size)
                    block.draw(block_info, color, line)

                distance -= move

            else:
                block_info = ((start_x) + i * (block_size + blank), start_y, block_size, block_size)
                block.draw(block_info, color, line)
        pygame.display.update()
        if done == True:
            break


def show_selection(data_list):
    global index, selection_process
    index = 0
    selection_process = selection_result(data_list)
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        selection_process[index][0](selection_process[index][1], selection_process[index][2], selection_process[index][3])
        pygame.display.update()



def selection_result(data_list):
    global index, selection_process
    result = []
    for i in range(len(data_list) - 1):
        min_position = i
        for k in range(i + 1, len(data_list)):
            if data_list[k] < data_list[min_position]:
                min_position = k

        if min_position != i:
            tmp = data_list[i]
            data_list[i] = data_list[min_position]
            data_list[min_position] = tmp

    return result


def selection_draw(data_list, tmp, min, color=BLACK, line=10):
    global index, selection_process
    (start_x, start_y, block_size, blank) = checkBlock(data_list)
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)
        done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT:
                    if index > 0:
                        index -= 1
                        done = True

                elif event.key == pygame.K_RIGHT:
                    if index < len(selection_process) - 1:
                        index += 1
                        done = True


def selection_change(data_list, tmp, min, color=BLACK, line=10):
    global index, selection_process
    (start_x, start_y, block_size, blank) = checkBlock(data_list)
    while True:
        clock.tick(60)
        screen.fill(YELLOW_BRIGHT)
        done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT:
                    if index > 0:
                        index -= 1
                        done = True

                elif event.key == pygame.K_RIGHT:
                    if index < len(selection_process) - 1:
                        index += 1
                        done = True


# 정렬 과정을 순서대로 리스트에 담기
# 리스트에 들어갈 원소의 내용은 함수 이름과 매개변수 값
# 오른쪽 키 누르면 다음 원소 실행, 왼쪽 키 누르면 이전 원소 실행

# 메인 화면 -> 리스트에 들어갈 원소 선택(1~50) (길이가 3 미만 10 초과면 다음 단계 실행 막기)
# -> 정렬 or 탐색 선택 -> 실행
while True:
    clock.tick(60)
    screen.fill(YELLOW_BRIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    a = Block(10)
    b = Block(8)
    c = Block(4)
    d = Block(9)
    e = Block(6)

    my_list = [a, b, c, d, e]

    show_bubble(my_list)

    pygame.display.update()

pygame.quit()
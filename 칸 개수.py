# 시작 y값: 300 - (칸 크기 / 2)

# 앞 뒤로 80px 남기기
# 계산 공식: (1140 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
# 10개 일 때, 칸: 96px, 간격: 20px, 시작 y:
# 9개 일 때, 칸: 104.5px, 간격: 25px
# 8개 일 때, 칸: 116.25px, 간격: 30px
# 7개 일 때, 칸: 132.85px, 간격: 35px

# 앞 뒤로 150px 남기기
# 계산 공식: (1000 - (간격 * (칸 개수 -1))) / 칸 개수 == 칸의 크기
# 6개 일 때, 칸: 137.5px, 간격: 35px
# 5개 일 때, 칸: 160px, 간격: 50px


def solve1(length, blank):
    return (1140 - (blank * (length - 1))) / length

def solve2(length, blank):
    return (1000 - (blank * (length - 1))) / length

def start_y(size):
    return 300 - (size/2)


# print(solve1(7, 35))
print(solve2(5, 50))
print(start_y(168))
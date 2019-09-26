# 시작 y값: 300 - (칸 크기 / 2)
def start_y(size):
    return 300 - (size/2)

print(start_y(150))

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


def solve1(length, blank):
    return (1140 - (blank * (length - 1))) / length

def solve2(length, blank):
    return (1000 - (blank * (length - 1))) / length

def solve3(length, blank):
    return (900 - (blank * (length - 1))) / length

def solve4(length, blank):
    return (700 - (blank * (length - 1))) / length




# print(solve1(7, 35))
# print(solve2(5, 65))
# print(solve3(4, 100))
# print(solve4(3, 125))

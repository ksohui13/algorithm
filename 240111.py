# 프로그래머스

#[PCCE 기출문제] 1번 / 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/250133

string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")


# [PCCE 기출문제] 2번 / 피타고라스의 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/250132

a = int(input())
c = int(input())

b_square = c**2 - a**2
print(b_square)

# [PCCE 기출문제] 3번 / 나이 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/250131

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2031-year
elif age_type == "Year":
    answer = 2030-year

print(answer)

# [PCCE 기출문제] 4번 / 저축
# https://school.programmers.co.kr/learn/courses/30/lessons/250130

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1

while money < 100 :
    money += after
    month += 1
print(month)

# [PCCE 기출문제] 5번 / 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/250129

def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W" :
            east -= 1
    return [east, north]

# [PCCE 기출문제] 6번 / 가채점
# https://school.programmers.co.kr/learn/courses/30/lessons/250128

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

# [PCCE 기출문제] 7번 / 가습기
# https://school.programmers.co.kr/learn/courses/30/lessons/250127

def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer

# [PCCE 기출문제] 8번 / 창고 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/250126

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])

# [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def in_range(x, y, n):
    return (0 <= x < n and 0 <= y < n)


def solution(board, h, w):
    answer = 0
    dhs = [0, 1, -1, 0]
    dws = [1, 0, 0, -1]
    
    for dh, dw in zip(dhs, dws):
        nh, nw = h + dh, w + dw
        if not in_range(nh, nw, len(board)):
            continue
        if board[h][w] == board[nh][nw]:
            answer += 1
            
    return answer

#다른 풀이
def solution(board, h, w):
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    target = board[h][w]
    n = len(board)

    answer = 0
    for d in range(4):
        nh, nw = h+dh[d], w+dw[d]
        if 0 <= nh < n and 0 <= nw < n and target == board[nh][nw]:
            answer += 1

    return answer

# [PCCE 기출문제] 10번 / 데이터 분석
# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    data_type = {"code":0, "date":1, "maximum":2, "remain":3}

    filter_data = [d for d in data if d[data_type[ext]] < val_ext]

    sorted_filter_data = sorted(filter_data, key=lambda x:x[data_type[sort_by]])

    return sorted_filter_data


#다른 풀이
def solution(data, ext, val_ext, sort_by):

    if ext == "code": newExt = 0
    elif ext == "date": newExt = 1
    elif ext == "maximum": newExt = 2
    else: newExt = 3

    if sort_by == "code": newSort = 0
    elif sort_by == "date": newSort = 1
    elif sort_by == "maximum": newSort = 2
    else: newSort = 3

    answer = []
    for d in data:
        if d[newExt] < val_ext:
            answer.append(d)

    return sorted(answer, key=lambda x: x[newSort])
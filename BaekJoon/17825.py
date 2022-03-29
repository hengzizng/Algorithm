'''
# Solution 1 >
from collections import defaultdict
import sys
read = sys.stdin.readline


# 말이 다음에 도착할 칸을 구한다. (이동 불가능하면 -1 반환)
# meeple: 말의 현재 위치, number: 주사위의 수
def get_next_node(meeple, number, is_meeple):
    # 파란색 칸에서 출발한다면 (현재 위치가 파란색 칸이라면)
    if meeple == 5 or meeple == 10 or meeple == 15:
        next_node = max(next_nodes[meeple])
    else:
        next_node = next_nodes[meeple][0]

    for _ in range(number):
        meeple = next_node
        # 도착점에 도착했다면 이동 종료
        if meeple == BOARD_SIZE - 1:
            break
        next_node = min(next_nodes[meeple])
    
    if is_meeple[meeple]: # 이동한 칸에 다른 말이 있다면
        return -1
    else:
        return meeple


# 말 하나가 움직인다.
# count: 이동 횟수, m1~m4: 말들의 위치
def move(count, m1, m2, m3, m4, score_sum):
    if score_sum + ((10 - count) * MAX_SCORE) < max_score_sum[0]:
        return

    if count == 10:
        max_score_sum[0] = max(max_score_sum[0], score_sum)
        return

    # 각 칸에 말이 위치해있는지 여부
    is_meeple = [False] * BOARD_SIZE
    is_meeple[m1] = True
    is_meeple[m2] = True
    is_meeple[m3] = True
    is_meeple[m4] = True
    is_meeple[BOARD_SIZE - 1] = False

    if m1 < BOARD_SIZE - 1:
        new_m1 = get_next_node(m1, numbers[count], is_meeple)
        if new_m1 > -1:
            move(count + 1, new_m1, m2, m3, m4, score_sum + scores[new_m1])

    if m2 < BOARD_SIZE - 1:
        new_m2 = get_next_node(m2, numbers[count], is_meeple)
        if new_m2 > -1:
            move(count + 1, m1, new_m2, m3, m4, score_sum + scores[new_m2])

    if m3 < BOARD_SIZE - 1:
        new_m3 = get_next_node(m3, numbers[count], is_meeple)
        if new_m3 > -1:
            move(count + 1, m1, m2, new_m3, m4, score_sum + scores[new_m3])

    if m4 < BOARD_SIZE - 1:
        new_m4 = get_next_node(m4, numbers[count], is_meeple)
        if new_m4 > -1:
            move(count + 1, m1, m2, m3, new_m4, score_sum + scores[new_m4])


# 게임판 내 칸의 개수 (시작, 도착 포함)
BOARD_SIZE = 33
# 칸에 적힌 점수 중 최대 점수
MAX_SCORE = 40

# 각 칸마다의 점수
scores = list(range(0, 40 + 1, 2))
scores.extend([13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0])

# 각 칸마다의 다음 칸 (0: 시작, 32: 도착)
next_nodes = defaultdict(list)
for node in range(20):
    next_nodes[node].append(node + 1)

next_nodes[5].append(21)
next_nodes[21].append(22)
next_nodes[22].append(23)
next_nodes[23].append(29)

next_nodes[10].append(24)
next_nodes[24].append(25)
next_nodes[25].append(29)

next_nodes[15].append(26)
next_nodes[26].append(27)
next_nodes[27].append(28)
next_nodes[28].append(29)

next_nodes[29].append(30)
next_nodes[30].append(31)
next_nodes[31].append(20)
next_nodes[20].append(32)

# 주사위에서 나올 수 10개
numbers = list(map(int, read().split()))

# 점수의 최댓값
max_score_sum = [0]

move(0, 0, 0, 0, 0, 0)

print(max_score_sum[0])
'''

# Solution 2 >
import sys
read = sys.stdin.readline


def move(count, score_sum):
    if score_sum + ((10 - count) * MAX_SCORE) < max_score_sum[0]:
        return

    if count == 10:
        max_score_sum[0] = max(max_score_sum[0], score_sum)
        return

    # 각 말별로 이동
    for meeple in range(4):
        # now_pos: 현재 위치, next_pos: 이동할 위치, number: 이동할 칸 수
        now_pos, next_pos, number = meeples[meeple], meeples[meeple], numbers[count]

        # 파란색 칸에서 시작한다면
        if now_pos == 5 or now_pos == 10 or now_pos == 15:
            next_pos = blue_path[now_pos]
            number -= 1
        
        # number만큼 이동
        for _ in range(number):
            next_pos = red_path[next_pos]
        
        # 다음에 갈 위치가 도착점이 아닌데 다른 말이 있다면 못감
        if next_pos != 21 and is_meeple[next_pos]:
            continue

        is_meeple[now_pos], is_meeple[next_pos], meeples[meeple] = False, True, next_pos
        move(count + 1, score_sum + scores[next_pos])
        is_meeple[now_pos], is_meeple[next_pos], meeples[meeple] = True, False, now_pos


# red_path[index]: index에서 다음으로 갈 칸 (빨간색 선)
# 시작: 0, 도착: 21
red_path = [0] * 33
for i in range(21):
    red_path[i] = i + 1
red_path[21] = 21 # 도착
red_path[22], red_path[23], red_path[24] = 23, 24, 30 # 왼쪽에서 중앙으로
red_path[25], red_path[26] = 26, 30 # 아래쪽에서 중앙으로
red_path[27], red_path[28], red_path[29] = 28, 29, 30 # 오른쪽에서 중앙으로
red_path[30], red_path[31], red_path[32] = 31, 32, 20 # 중앙에서 위쪽으로

# blue_path[index]: index에서 다음으로 갈 칸 (파란색 선)
blue_path = [0] * 16
blue_path[5], blue_path[10], blue_path[15] = 22, 25, 27

# 각 칸마다의 점수
scores = list(range(0, 40 + 1, 2))
scores.extend([0, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35])

# 주사위에서 나올 수 10개
numbers = list(map(int, read().split()))

# meeples: 말들의 위치, is_meeple: 말들이 위치해있는지 여부
meeples, is_meeple = [0] * 4, [False] * 33

# 칸에 적힌 점수 중 최대 점수
MAX_SCORE = 40

# 숫자들의 합의 최댓값
max_score_sum = [0]

move(0, 0)

print(max_score_sum[0])
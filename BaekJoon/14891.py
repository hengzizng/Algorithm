# 톱니바퀴는 4개 (가장 왼쪽이 1번)
# 톱니바퀴의 톱니는 8개 (각 톱니는 N극(0) or S극(1))
# 톱니바퀴 회전 수 K (K칸 이동)
# 회전은 시계방향(1) or 반시계방향(-1)

# 톱니바퀴끼리 닿는 위치(인덱스)
# 1번의 2 - 2번의 6
# 2번의 2 - 3번의 6
# 3번의 2 - 4번의 6


import sys
from collections import deque
read = sys.stdin.readline


def rotate_by_direction(gear_no, direction):
    if direction == 1:  # 시계 방향
        gears[gear_no].appendleft(gears[gear_no].pop())
    else:  # 반시계 방향
        gears[gear_no].append(gears[gear_no].popleft())


def rotate_all(gear_no, direction):
    rotate_list = [(gear_no, direction)]

    # 회전시킬 톱니바퀴의 오른쪽 톱니바퀴들을 회전시킨다
    now_direction = direction
    for right in range(gear_no + 1, 4 + 1):
        now_direction = now_direction * -1
        if gears[right - 1][2] == gears[right][6]:
            break
        else:
            rotate_list.append((right, now_direction))

    # 회전시킬 톱니바퀴의 왼쪽 톱니바퀴들을 회전시킨다
    now_direction = direction
    for left in range(gear_no - 1, 1 - 1, -1):
        now_direction = now_direction * -1
        if gears[left][2] == gears[left + 1][6]:
            break
        else:
            rotate_list.append((left, now_direction))

    for now in rotate_list:
        rotate_by_direction(*now)


gears = [[]]  # 톱니바퀴들의 상태
for _ in range(4):
    gears.append(deque(map(int, list(read().strip()))))

K = int(read())  # 회전 횟수
for _ in range(K):
    rotate_all(*map(int, read().split()))  # (회전시킨 톱니바퀴 번호, 회전 방향)

# 네 톱니바퀴의 점수의 합을 구한다
score = 0
for index in range(4):
    score += gears[index + 1][0] * (1 << index)
print(score)

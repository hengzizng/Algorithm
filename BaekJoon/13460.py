# 빨간구슬 구멍으로 O, 파란구슬은 구멍으로 X, 동시에 구멍으로 X
# 더이상 구슬이 움직이지 않을때까지 기울이는 동작 진행

# 최소 몇번만에 빨간 구슬을 구멍에 넣을 수 있는지
# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1

# 행 수 N, 열 수 M
# .: 구슬이 이동 가능, #: 구슬이 이동 불가능, O: 구멍, R: 빨간구슬, B: 파란구슬

from collections import deque
import sys
read = sys.stdin.readline


# 기울일 방향을 정하는 함수
def set_direction(balls):
    checked = set([balls])
    queue = deque([(*balls, 0)])

    while queue:
        now = queue.popleft()
        balls = (now[0], now[1], now[2], now[3])

        for index in range(3 + 1):  # 방향 0 ~ 3 중 하나를 선택
            new_balls = move_all(index, balls)  # 선택한 방향대로 구슬들을 이동

            if now[4] + 1 >= min_count[0] or new_balls in checked:  # 11번 이상이면 확인할 필요 X
                continue

            checked.add(new_balls)

            if new_balls[0] == -1 and new_balls[1] == -1:  # 빨간 구슬이 구멍에 도착
                if new_balls[2] == -1 and new_balls[3] == -1:  # 파란 구슬이 구멍에 도착
                    continue
                else:  # 파란 구슬은 구멍이 아닌 다른 위치
                    min_count[0] = now[4] + 1
                    queue.clear()
                    break

            queue.append((*new_balls, now[4] + 1))


# 구슬들을 방향대로 옮기고 그 위치를 리턴하는 함수
def move_all(direction, balls):
    # 위치, 구멍에 도달했는지 여부
    red = [balls[0], balls[1]]
    blue = [balls[2], balls[3]]

    if direction == 0:  # 북쪽으로 이동이면 더 위에 있는 구슬이 먼저 이동
        if balls[0] < balls[2]:  # 빨간색 먼저 이동
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란색 먼저 이동
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    elif direction == 1:  # 남쪽으로 이동이면 더 아래에 있는 구슬이 먼저 이동
        if balls[0] > balls[2]:  # 빨간색 먼저 이동
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란색 먼저 이동
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    elif direction == 2:  # 서쪽으로 이동이면 더 왼쪽에 있는 구슬이 먼저 이동
        if balls[1] < balls[3]:  # 빨간색 먼저 이동
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란색 먼저 이동
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    else:  # 동쪽으로 이동이면 더 오른쪽에 있는 구슬이 먼저 이동
        if balls[1] > balls[3]:  # 빨간색 먼저 이동
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란색 먼저 이동
            move_one(direction, blue, red)
            move_one(direction, red, blue)

    return (*red, *blue)


# 구슬 하나를 움직이는 함수
def move_one(direction, target, other):
    is_hole = False

    while True:
        target[0] += dr[direction]
        target[1] += dc[direction]

        if board[target[0]][target[1]] == 'O':
            is_hole = True
            break

        if board[target[0]][target[1]] == '#' or (target[0] == other[0] and target[1] == other[1]):
            break

    if is_hole:  # 구멍에 빠졌으면 공을 없애준다
        target[0], target[1] = -1, -1
    else:
        target[0] -= dr[direction]
        target[1] -= dc[direction]


# 북, 남, 서, 동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

min_count = [11]

board, temp = [], [-1, -1, -1, -1]
N, M = map(int, read().split())
for n in range(N):
    board.append(list(read().strip()))
    for m in range(M):
        if board[n][m] == 'R':
            temp[0], temp[1] = n, m
        elif board[n][m] == 'B':
            temp[2], temp[3] = n, m

balls = tuple(temp)

set_direction(balls)

if min_count[0] == 11:
    min_count[0] = -1

print(*min_count)

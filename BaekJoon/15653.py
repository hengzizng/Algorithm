# 빨간 구슬만 구멍에 빠져야 성공
# 파란 구슬이 구멍에 빠지면 실패

# 최소 몇 번만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지
# 어떻게 움직여도 불가능하면 -1

# 구슬들의 위치로 bfs 진행
# 이번에 어떤 방향으로 기울일지 정한다
# 방향에 따라 먼저 움직여야 할 구슬부터 움직인 뒤 다음 구슬이 움직인다

import sys
from collections import deque

read = sys.stdin.readline


def do(balls):
    queue, checked = deque(), set()

    queue.append((*balls, 0))
    checked.add(balls)

    while queue:
        now = queue.popleft()

        for direction in range(4):  # 이번에 움직힐 방향 (0 ~ 3)
            next_balls = move(direction, now)

            if next_balls in checked:  # 움직인 구슬들의 위치가 이미 해봤던 위치라면
                continue

            checked.add(next_balls)

            if next_balls[2] == -1 and next_balls[3] == -1:  # 파란 구슬이 구멍에 빠졌으면
                continue

            if next_balls[0] == -1 and next_balls[1] == -1:  # 빨간 구슬이 구멍에 빠졌으면
                return now[4] + 1

            queue.append((*next_balls, now[4] + 1))

    return -1


# 구슬들이 움직인 뒤 그 위치를 반환 (구멍에 빠졌다면 -1, -1 반환)
def move(direction, balls):
    red, blue = [balls[0], balls[1]], [balls[2], balls[3]]

    if direction == 0:  # 움직일 방향이 북쪽이면 더 위에 위치한 구슬부터 움직인다
        if balls[0] < balls[2]:  # 빨간 구슬 먼저
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란 구슬 먼저
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    elif direction == 1:  # 움직일 방향이 남쪽이면 더 아래에 위치한 구슬부터 움직인다
        if balls[0] > balls[2]:  # 빨간 구슬 먼저
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란 구슬 먼저
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    elif direction == 2:  # 움직일 방향이 서쪽이면 더 왼쪽에 위치한 구슬부터 움직인다
        if balls[1] < balls[3]:  # 빨간 구슬 먼저
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란 구슬 먼저
            move_one(direction, blue, red)
            move_one(direction, red, blue)
    else:  # 움직일 방향이 동쪽이면 더 오른쪽에 위치한 구슬부터 움직인다
        if balls[1] > balls[3]:  # 빨간 구슬 먼저
            move_one(direction, red, blue)
            move_one(direction, blue, red)
        else:  # 파란 구슬 먼저
            move_one(direction, blue, red)
            move_one(direction, red, blue)

    return (*red, *blue)


# 구슬 하나를 움직이는 함수
def move_one(direction, target, other):
    while True:
        temp = board[target[0]][target[1]]

        if temp == "O":
            target[0], target[1] = -1, -1
            break

        if temp == "#" or (target[0] == other[0] and target[1] == other[1]):
            break

        target[0] += drdc[direction][0]
        target[1] += drdc[direction][1]

    if target[0] > -1:  # 구멍에 빠진게 아니라면
        target[0] -= drdc[direction][0]
        target[1] -= drdc[direction][1]


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 북, 남, 서, 동


N, M = map(int, read().split())  # 행 수 N, 열 수 M
board, balls = [], [-1] * 4
for n in range(N):
    board.append(list(read().strip()))
    for m in range(M):
        if board[n][m] == "R":
            balls[0], balls[1] = n, m
        elif board[n][m] == "B":
            balls[2], balls[3] = n, m
balls = tuple(balls)


print(do(balls))

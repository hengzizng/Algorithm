# 37 min

# 사과를 먹으면 뱀 길이 길어짐

# 뱀이 벽 or 자신의 몸 과 부딪히면 게임 종료

# N x N 크기의 보드
# 보드의 둘레에는 벽이 있다

# 뱀 시작 위치 : 맨 위 맨 왼쪽
# 뱀 시작 길이 : 1
# 뱀 시작 방향 : 오른쪽

# 뱀의 이동
# 몸길이를 늘려 머리를 다음 칸에
# 만약 이동한 칸에
#   사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
#   사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비운다 -> 몸 길이는 변하지 않음 (한칸 이동한것과 같다)

# 사과의 위치, 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지


from collections import deque
import sys
read = sys.stdin.readline


def turn_left(direction):
    return (direction + 3) % 4

def turn_right(direction):
    return (direction + 1) % 4


# 방향 - 0: 상, 1: 우, 2: 하, 3: 좌
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N = int(read()) # 보드의 크기
board = [[0] * N for _ in range(N)] # 사과: 1, 뱀: 2

K = int(read()) # 사과의 개수
for _ in range(K):
    row, col = map(lambda x: int(x) - 1, read().split())
    board[row][col] = 1

L = int(read()) # 뱀의 방향 변환 횟수
info = {}
for _ in range(L):
    # X: 시간 (초), C: 회전 방향 (L: 왼쪽, D: 오른쪽)
    X, C = read().strip().split()
    info[int(X)] = C

# snake (deque)
#  ------------------
# ㅣ꼬리         머리
#  ------------------
snake = deque([(0, 0)])
board[0][0] = 2
direction = 1
time = 0
while True:
    time += 1

    head = snake[-1]
    nr, nc = head[0] + drdc[direction][0], head[1] + drdc[direction][1]

    # 벽과 만나거나 자신의 몸과 만나면 게임 종료
    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
        break

    # 이동한 칸에 사과가 없다면 꼬리 이동
    if board[nr][nc] == 0:
        tail = snake.popleft()
        board[tail[0]][tail[1]] = 0

    board[nr][nc] = 2
    snake.append((nr, nc))

    # time 초가 끝난 뒤에 방향 변환 정보에 따라 방향 전환
    if time in info:
        if info[time] == "L":
            direction = turn_left(direction)
        else:
            direction = turn_right(direction)
    
print(time)
from heapq import *
import sys

read = sys.stdin.readline


def is_valid(r, c):
    if 0 <= r < H and 0 <= c < W and board[r][c] != '*':
        return True
    return False


# 상, 우, 하, 좌
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# W: 너비, H: 높이
W, H = map(int, read().split())
# board 값: . 빈칸, * 벽, C 레이저로 연결할 두 칸
board = [list(read().strip()) for _ in range(H)]
# targets: 레이저로 연결할 두 칸의 행, 열 좌표
targets = []
for r in range(H):
    for c in range(W):
        if board[r][c] == 'C':
            targets.append([r, c])

# turn_counts[r][c][d]: 방향별로 target 1부터 각 위치까지 경로들 중 최소 방향전환 횟수
turn_counts = [[[W * H] * 4 for _ in range(W)] for _ in range(H)]

# (방향전환 횟수, 행, 열, 방향)
pq = [(0, *targets[0], 0), (0, *targets[0], 1),
      (0, *targets[0], 2), (0, *targets[0], 3)]
while pq:
    turn_count, r, c, d = heappop(pq)

    if turn_count >= turn_counts[r][c][d]:
        continue

    turn_counts[r][c][d] = turn_count

    if r == targets[1][0] and c == targets[1][1]:
        break

    # 현재 진행방향으로 이동
    nr, nc = r + drdc[d][0], c + drdc[d][1]
    if is_valid(nr, nc):
        heappush(pq, (turn_count, nr, nc, d))

    # 시계 방향으로 90도 회전해서 이동
    nd = (d + 1) % 4
    nr, nc = r + drdc[nd][0], c + drdc[nd][1]
    if is_valid(nr, nc):
        heappush(pq, (turn_count + 1, nr, nc, nd))

    # 반시계 방향으로 90도 회전해서 이동
    nd = (d + 3) % 4
    nr, nc = r + drdc[nd][0], c + drdc[nd][1]
    if is_valid(nr, nc):
        heappush(pq, (turn_count + 1, nr, nc, nd))

print(min(turn_counts[targets[1][0]][targets[1][1]]))

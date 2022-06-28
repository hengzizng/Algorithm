from collections import deque
import sys
read = sys.stdin.readline


def melt():
    queue = deque([(0, 0)])

    while queue:
        now = queue.popleft()

        for nr, nc in drdc:
            nr, nc = nr + now[0], nc + now[1]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or status[nr][nc] == -1:
                continue

            # 공기와 인접
            if board[nr][nc] == 0:
                queue.append((nr, nc))
                status[nr][nc] = -1
            # 치즈와 인접
            else:
                status[nr][nc] += 1

    # 치즈가 녹는다.
    zero_count = 0
    for r in range(N):
        for c in range(M):
            if status[r][c] >= 2:
                board[r][c] = 0
            status[r][c] = 0

            if board[r][c] == 0:
                zero_count += 1

    # 치즈가 다 녹았을 경우 true 반환
    if zero_count == N * M:
        return True
    else:
        return False


drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 모눈종이의 크기
N, M = map(int, read().split())
# 모눈종이 (치즈 상태)
board = [list(map(int, read().split())) for _ in range(N)]
# -1: 방문한 공기, 0: 방문하지 않음, 1이상: 치즈가 공기에 닿은 횟수
status = [[0] * M for _ in range(N)]

for time in range(1, N * M):
    if melt():
        print(time)
        break

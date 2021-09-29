"""
from collections import deque
import sys
read = sys.stdin.readline


def bfs():
    queue = deque()
    visited = set()

    queue.append((0, 0, 1))
    visited.add((0, 0))

    while queue:
        x, y, dist = queue.popleft()

        # 현재 위치에서 최소 거리로 이동해도 이미 구한 값보다 크다면
        if dist + (N - x - 1) + (M - y - 1) > min_dist:
            return N * M
        
        for dx, dy in dxdy:
            dx += x
            dy += y
            
            if dx == N - 1 and dy == M - 1: # 목적지에 도달했다면
                return dist + 1

            if (
                0 <= dx < N and 0 <= dy < M and
                board[dx][dy] == 0 and (dx, dy) not in visited
                ):

                visited.add((dx, dy))
                queue.append((dx, dy, dist + 1))

    return N * M


N, M = map(int, read().split()) # 행 수, 열 수
board = []
for _ in range(N):
    board.append(list(map(int, list(read().strip()))))

dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
min_dist = N * M

for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            board[n][m] = 0
            min_dist = min(min_dist, bfs())
            board[n][m] = 1

print(-1 if min_dist == N * M else min_dist)
"""



from collections import deque
import sys
read = sys.stdin.readline


def bfs():
    if N == 1 and M == 1:
        return 1

    dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    min_dist = N * M

    queue = deque()
    # visited의 3차원 배열 - 0일때의 값: 벽을 부수지 않고 방문, 1일때의 값: 벽을 부수고 방문
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    queue.append((0, 0, 1, 0)) # (x, y, 거리, 이전에 벽을 부쉈는지 여부(0: X, 1: O))
    visited[0][0][0] = True

    while queue:
        x, y, dist, is_destroy = queue.popleft()
        
        for dx, dy in dxdy:
            dx += x
            dy += y
            
            if dx == N - 1 and dy == M - 1: # 목적지에 도달했다면
                return dist + 1

            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy][is_destroy]:
                if board[dx][dy] == 0: # 벽이 아니라면
                    visited[dx][dy][is_destroy] = True
                    queue.append((dx, dy, dist + 1, is_destroy))
                else: # 벽이 있는 곳이라면
                    if is_destroy == 0: # 지금까지의 경로에서 벽을 부순 적이 없다면 이번에 부수고 방문
                        visited[dx][dy][1] = True
                        queue.append((dx, dy, dist + 1, 1))

    return -1


N, M = map(int, read().split()) # 행 수, 열 수
board = []
for _ in range(N):
    board.append(list(map(int, list(read().strip()))))

print(bfs())
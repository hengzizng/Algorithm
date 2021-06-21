from collections import deque
import sys
read = sys.stdin.readline

# M: 행 수, N: 열 수, K: 직사각형 수
M, N, K = map(int, read().split())
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(grid, x, y):
    queue = deque([(x, y)])
    grid[x][y] = 1

    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1

        for next_x, next_y in direction:
            next_x, next_y = next_x + x, next_y + y
            if (
                0 <= next_x < M and
                0 <= next_y < N and
                grid[next_x][next_y] == 0
            ):
                grid[next_x][next_y] = 1
                queue.append((next_x, next_y))

    return count


grid = [[0] * N for _ in range(M)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, read().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

count = 0
area = []
for x in range(M):
    for y in range(N):
        if grid[x][y] == 0:
            area.append(bfs(grid, x, y))
            count += 1

area.sort()
print(count)
print(' '.join(map(str, area)))
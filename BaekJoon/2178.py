from collections import deque
from sys import stdin


# time_out_bfs : 처음 작성한 시간 초과 함수
def time_out_bfs(row, col, path):
    queue = deque()

    queue.append((row, col, path))
    while queue:
        row, col, path = queue.popleft()
        maze[row][col] = 0
        if row == N - 1 and col == M - 1:
            break
        if row - 1 >= 0 and maze[row-1][col] == 1:
            queue.append((row-1, col, path+1))
        if row + 1 <= N - 1 and maze[row+1][col] == 1:
            queue.append((row+1, col, path+1))
        if col - 1 >= 0 and maze[row][col-1] == 1:
            queue.append((row, col-1, path+1))
        if col + 1 <= M - 1 and maze[row][col+1] == 1:
            queue.append((row, col+1, path+1))

    return path

# bfs : 실제출 정답
def bfs(row, col, path):
    queue = deque()

    queue.append((row, col, path))
    while queue:
        row, col, path = queue.popleft()
        if row == N - 1 and col == M - 1:
            break

        if row < 0 or row > N - 1 or \
           col < 0 or col > M - 1 or \
           maze[row][col] != 1:
           continue

        maze[row][col] = 0
        queue.append((row-1, col, path+1))
        queue.append((row+1, col, path+1))
        queue.append((row, col-1, path+1))
        queue.append((row, col+1, path+1))

    return path
    

N, M = map(int, input().split())  # N: 행, M: 열
maze = [[]] * N
for row in range(N):
    maze[row] = list(map(int, stdin.readline().strip()))

print(bfs(0, 0, 1))